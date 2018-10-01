import numpy as np
from scipy import interpolate
import copy
import webrtcvad
import random
import os
import subprocess
import tempfile
import json
import soundfile as sf


def __sox(y, sr, *args):
    '''Execute sox
    Parameters
    ----------
    y : np.ndarray
        Audio time series
    sr : int > 0
        Sampling rate of `y`
    *args
        Additional arguments to sox
    Returns
    -------
    y_out : np.ndarray
        `y` after sox transformation
    '''

    assert sr > 0

    fdesc, infile = tempfile.mkstemp(suffix='.wav')
    os.close(fdesc)
    fdesc, outfile = tempfile.mkstemp(suffix='.wav')
    os.close(fdesc)

    # Dump the audio
    sf.write(infile, y, sr)

    try:
        arguments = ['sox', infile, outfile, '-q']
        arguments.extend(args)

        subprocess.check_call(arguments)

        y_out, sr = sf.read(outfile)

    finally:
        os.unlink(infile)
        os.unlink(outfile)

    return y_out


def drc(y, sr, preset):
    '''Apply a preset DRC
    Parameters
    ----------
    y : np.ndarray
        Audio time series
    sr : int > 0
        Sampling rate of `y`
    preset : str
        Preset keyword (see PRESETS)
    Returns
    -------
    y_out : np.ndarray
        `y` after applying preset DRC
    '''

    return __sox(y, sr, 'compand', *PRESETS[preset])


def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_product(*args, **kwds):
    "Random selection from itertools.product(*args, **kwds)"
    pools = map(tuple, args) * kwds.get('repeat', 1)
    return tuple(random.choice(pool) for pool in pools)


def pad_tracks(tracks, maxlen=None,
               padding='post', truncating='post', value=0.):
    '''pad or trim tracks,

    maxlen of -1 does trim to minimum value,
    maxlen None trims to maximum value
    any other values trims to that value or pads to get to that value
'''
    lengths = [array['audio'].shape[0] for array in tracks]

    if maxlen is None:
        maxlen = np.max(lengths)
    elif maxlen == -1:
        maxlen = np.min(lengths)

    for idx, s in enumerate(tracks):
        x = (np.ones((maxlen,)) * value)

        if truncating == 'pre':
            trunc = s['audio'][-maxlen:]
        elif truncating == 'post':
            trunc = s['audio'][:maxlen]
        else:
            raise ValueError('Truncating "%s" not understood' % truncating)

        # check `trunc` has expected shape
        trunc = np.asarray(trunc)

        if padding == 'post':
            x[:len(trunc)] = trunc
        elif padding == 'pre':
            x[-len(trunc):] = trunc
        else:
            raise ValueError('Padding type "%s" not understood' % padding)

        tracks[idx]['audio'] = x

    return tracks, maxlen


def has_speech(audio, rate):
    speech = vad(audio, rate, sensitivity=3)
    speech_elements = np.count_nonzero(speech)
    return float(speech_elements) / speech.shape[0] > 0.1


def remove_silence(audio, rate):
    activation = vad(audio, rate)
    activation = interp(activation, audio.shape[0]).astype(np.bool)
    active_elements = np.nonzero(activation)[0]
    start = active_elements[0]
    end = active_elements[-1]
    return audio[start:end]


def vad(input_audio, rate, sensitivity=1):
    # convert to 16bit signed int
    audio = np.int16(input_audio * 32767)
    vad = webrtcvad.Vad()

    # mode 3 (max=3) means, very sensitive regarding to non-speech
    vad.set_mode(sensitivity)

    # window size 10ms
    n = int(rate * 0.01)

    # window without overlap
    chunks = list(
        audio[pos:pos + n] for pos in range(0, len(audio), n)
    )
    if len(chunks[-1]) != n:
        chunks = chunks[:-1]

    voiced = []
    for chunk in chunks:
        voiced.append(vad.is_speech(chunk.tobytes(), rate))

    return np.array(voiced)


def no_activations(X, max_count=36):
    # fill activations
    return np.zeros(
        (X.shape[0], max_count),
        dtype=np.int
    )


def track_activations(tracks, X, speakers_table, sensitivity=1, max_count=36):

    # init activation matrix
    H = []
    for track in tracks:
        H.append(vad(track['audio'], track['rate'], sensitivity))

    # fill activations
    Y = np.zeros(
        (X.shape[0], max_count),
        dtype=np.int
    )

    for i, track in enumerate(tracks):
        # find index of track_id in table
        speaker_id = np.where(speakers_table == tracks[i]['id'])[0][0] + 1
        # fill stretched values
        Y[:, i] = interp(
            H[i] * speaker_id, X.shape[0]
        ).astype(np.int)

    return Y


def sliding_window(data, size, stepsize=1, padded=False, axis=-1, copy=True):
    """
    Calculate a sliding window over a signal
    Parameters
    ----------
    data : numpy array
        The array to be slided over.
    size : int
        The sliding window size
    stepsize : int
        The sliding window stepsize. Defaults to 1.
    axis : int
        The axis to slide over. Defaults to the last axis.
    copy : bool
        Return strided array as copy to avoid sideffects when manipulating the
        output array.
    Returns
    -------
    data : numpy array
        A matrix where row in last dimension consists of one instance
        of the sliding window.
    Notes
    -----
    - Be wary of setting `copy` to `False` as undesired sideffects with the
      output values may occurr.
    Examples
    --------
    >>> a = numpy.array([1, 2, 3, 4, 5])
    >>> sliding_window(a, size=3)
    array([[1, 2, 3],
           [2, 3, 4],
           [3, 4, 5]])
    >>> sliding_window(a, size=3, stepsize=2)
    array([[1, 2, 3],
           [3, 4, 5]])
    See Also
    --------
    pieces : Calculate number of pieces available by sliding
    """
    if axis >= data.ndim:
        raise ValueError(
            "Axis value out of range"
        )

    if stepsize < 1:
        raise ValueError(
            "Stepsize may not be zero or negative"
        )

    if size > data.shape[axis]:
        raise ValueError(
            "Sliding window size may not exceed size of selected axis"
        )

    shape = list(data.shape)
    shape[axis] = np.floor(
        data.shape[axis] / stepsize - size / stepsize + 1
    ).astype(int)
    shape.append(size)

    strides = list(data.strides)
    strides[axis] *= stepsize
    strides.append(data.strides[axis])

    strided = np.lib.stride_tricks.as_strided(
        data, shape=shape, strides=strides
    )

    if copy:
        return strided.copy()
    else:
        return strided


def interp(in_array, out_len, interpolation_type='nearest'):
    ''' stretch input array by output '''
    ip1d = interpolate.interp1d(
        np.arange(in_array.shape[0]),
        in_array,
        kind=interpolation_type
    )
    return ip1d(
        np.linspace(0, in_array.shape[0] - 1, out_len)
    ).astype(in_array.dtype)


def hwr(x):
    ''' half-wave rectification'''
    return (x + np.abs(x)) / 2


def reshape_for_sequences(
    X,
    y,
    batch_size,
    max_len,
    aggregate_output='max'
):
    """Reshape data according to batch size

    """

    X_s = np.atleast_3d(X)
    X_s = X_s.reshape(1, X_s.shape[0], X_s.shape[1])

    if y.ndim < 2:
        y = np.atleast_2d(y).T

    if max_len is not None:
        # reshape data into smaller chunks
        X_out = trim_multiple(
            X_s, (1, max_len, X_s.shape[-1])
        ).reshape(-1, max_len, X_s.shape[-1])

        # reshape data into smaller chunks
        y_out = trim_multiple(
            y, (max_len, y.shape[-1])
        ).reshape(-1, max_len, y.shape[-1])

        # apply reduction
        agg = getattr(np, aggregate_output)
        y_out = np.round(agg(y_out, axis=1)).astype(np.int32)

    return (X_out, y_out)


def reshape_for_sequences3d(
    X,
    y,
    batch_size,
    max_len,
    aggregate_output='max'
):
    """Reshape data according to batch size

    """
    X_s = np.copy(X)
    X_s = X_s.reshape(1, *X_s.shape)

    if y.ndim < 2:
        y = np.atleast_2d(y).T

    if max_len is not None:
        # reshape data into smaller chunks
        X_out = trim_multiple(
            X_s, (1, max_len, X_s.shape[-2], X_s.shape[-1])
        ).reshape(-1, max_len, X_s.shape[-2], X_s.shape[-1])
        X_out = X_out.transpose(0, 3, 1, 2)
        # reshape data into smaller chunks
        y_out = trim_multiple(
            y, (max_len, y.shape[-1])
        ).reshape(-1, max_len, y.shape[-1])

        # apply reduction
        agg = getattr(np, aggregate_output)
        y_out = np.round(agg(y_out, axis=1)).astype(np.int32)

    return (X_out, y_out)


def floor_multiple(num, divisor):
    """Floor to nearest common divisor.

    Arguments
    ---------
    num : int
    divisor : int

    >>> floor_multiple(2050, 1024)
    2048

    """
    return num - (num % divisor)


def safe_resize(data, shape):
    """Resize (shrink or grow) array without flattening the data.

    All data in the unaffected areas stays the same. Data is repeated along
    the dimensions of the data.

    Parameters
    ----------
    audio : array_like
        The input signal
    shape : tuple
        The desired output shape

    Returns
    -------
    out : array_like
        The reshaped signal

    Notes
    -----
     - For big data and large numbers of dimensions this function can get very
       slow.
     - You may not change the number of dimensions.

    """
    if len(data.shape) != len(shape):
        raise ValueError(
            "Data and target shape must be of same "
            "dimensionality"
        )

    tileshape = tuple(np.array(shape) // np.array(data.shape) + 1)
    data = np.tile(data, tileshape)

    sliceshape = tuple(slice(0, i) for i in shape)
    data = data[sliceshape]

    return data


def shift(tracks, track_overlap=0):
    # randomly overlap samples (conversations)
    overlaps = []
    out_tracks = copy.deepcopy(tracks)

    sum_of_samples = sum(array['audio'].shape[0] for array in tracks)

    for i in range(len(tracks) - 1):
        cur_overlap = int(min(
            tracks[i]['audio'].shape[0],
            tracks[i + 1]['audio'].shape[0]
        ) * track_overlap)
        overlaps.append(cur_overlap)

    overlaps.append(0)
    max_of_samples = max(array['audio'].shape[0] for array in tracks)

    sum_conversation_samples = max(
        sum_of_samples - sum(overlaps), max_of_samples
    )

    length = 0
    for i in range(len(tracks)):
        cur_track_len = tracks[i]['audio'].shape[0]

        end_pad = sum_conversation_samples - length - cur_track_len

        out_tracks[i]['audio'] = np.pad(
            out_tracks[i]['audio'],
            (length, end_pad),
            'constant'
        )

        length += cur_track_len - overlaps[i]

    return out_tracks


def mix(tracks):
    """Mix Audio to a minimum length of the audio files or max_len."""

    # all should have same length, so just add them
    audio_list = []
    for track in tracks:
        audio_list.append(track['audio'])

    audio_matrix = np.array(audio_list)
    out = np.sum(audio_matrix, axis=0)

    if np.any(out > 1.0):
        print("clipping!")

    return out


def train_valid_split(index_array, split, batch_size):
    """Split a index array into lower and upper half and returns both"""
    split_point = int((1 - split) * len(index_array))
    split_point -= split_point % batch_size

    train_indices = slice(
        0,
        split_point
    )
    validation_indices = slice(
        split_point,
        len(index_array)
    )
    train_index_array = index_array[train_indices]
    validation_index_array = index_array[validation_indices]

    return train_index_array, validation_index_array
