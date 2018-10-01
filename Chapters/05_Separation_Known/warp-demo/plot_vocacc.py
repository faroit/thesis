import numpy as np
import soundfile as sf
import seaborn as sns
import resampy
import librosa
import librosa.display
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os.path as op
import matplotlib as mpl
from matplotlib.patches import Patch
from matplotlib.ticker import Formatter, ScalarFormatter
import math
from matplotlib.transforms import BlendedGenericTransform
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap


def stft(
    audio,
    samplerate,
    resample_to=44100,
    n_fft=4096,
    hop_length=1024
):
    if resample_to != samplerate:
        audio = resampy.resample(audio, samplerate, resample_to)

    D = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length)

    return np.abs(D)


class TimeFormatter(Formatter):
    def __init__(self, hop_length=False, sr=None):
        self.hop_length = hop_length
        self.sr = sr

    def __call__(self, x, pos=None):
        return '{:.2g}'.format((x * self.hop_length) / self.sr)


def __coord_fft_hz(n, sr=44100):
    '''Get the frequencies for FFT bins'''
    n_fft = 2 * (n - 1)
    # The following code centers the FFT bins at their frequencies
    # and clips to the non-negative frequency range [0, nyquist]
    basis = librosa.core.fft_frequencies(sr=sr, n_fft=n_fft)
    fmax = basis[-1]
    basis -= 0.5 * (basis[1] - basis[0])
    basis = np.append(np.maximum(0, basis), [fmax])
    return basis


if __name__ == '__main__':

    # using the musdb color scheme
    # colors = ['w', '#56B4E9', '#009E73', '#964301', '#CC79A7']
    colors = ['w', '#FB9A29', '#662506']
    cmap = mpl.colors.ListedColormap(colors)

    mix_audio, rate = sf.read("files/mix.wav")
    mix_audio = np.mean(mix_audio, axis=1)

    S_mix = stft(mix_audio, rate, n_fft=4096, hop_length=1024).T

    # using the musdb color scheme
    # colors = ['w', '#56B4E9', '#009E73', '#964301', '#CC79A7']
    colors = ['w', '#FB9A29', '#662506']
    colors_sources = ['w', '#EE3377', '#33BBEE']
    cmap = mpl.colors.ListedColormap(colors)
    cmap_sources = mpl.colors.ListedColormap(colors_sources)

    reduce_bins = -1200
    y_axis = __coord_fft_hz(S_mix.shape[1], sr=rate)[:reduce_bins]
    x_axis = np.arange(S_mix.shape[0])

    # Get this from LaTeX using \showthe\columnwidth
    fig_width_pt = 244.6937
    # Convert pt to inch
    inches_per_pt = 1.0 / 72.27
    # Aesthetic ratio
    golden_mean = (math.sqrt(5) - 1.0) / 2.0
    # width in inches
    fig_width = fig_width_pt * inches_per_pt
    # height in inches
    fig_height = fig_width * golden_mean
    fig_size = np.array([fig_width*1.5, fig_height*1.5])

    params = {
        'backend': 'ps',
        'axes.labelsize': 18,
        'font.size': 15,
        'legend.fontsize': 16,
        'xtick.labelsize': 15,
        'ytick.labelsize': 15,
        'text.usetex': True,
        'font.family': 'serif',
        'font.serif': 'ptmrr8re',
        'figure.figsize': fig_size,
    }

    plt.rcParams.update(params)

    sns.set()
    sns.set_context("paper")

    sns.set_style("white", {
        'text.usetex': True,
        'font.family': 'serif',
        'axes.labelsize': 16,
        'font.size': 16,
        'legend.fontsize': 15,
        'xtick.labelsize': 17,
        'ytick.labelsize': 17,
        'figure.figsize': fig_size,
        'font.serif': 'ptmrr8re',
    })

    """
    Spectrogram (Mixture) Plot
    ########################################################################
    """
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)  # create an axes object in the figure
    ax.pcolormesh(
        x_axis, y_axis, np.log(S_mix[:, :reduce_bins].T + 0.5), cmap='gray_r', rasterized=True
    )
    # cb = f.colorbar(cax)
    ax.xaxis.set_major_formatter(TimeFormatter(hop_length=1024, sr=rate))
    ax.xaxis.set_label_text('Seconds')
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_label_text('Hz')

    f.set_tight_layout(True)
    f.savefig(
        "Mixture.pdf",
        rasterized=True,
        bbox_inches='tight',
        dpi=300
    )


    """
    Warped
    ########################################################################
    """

    warped_audio, rate = sf.read("files/vocals_warped.wav")
    warped_audio = np.mean(warped_audio, axis=1)

    S_ref = stft(warped_audio, rate, n_fft=4096, hop_length=1024).T

    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)  # create an axes object in the figure
    ax.pcolormesh(
        x_axis, y_axis, np.log(S_ref[:, :reduce_bins].T + 0.5), cmap='gray_r', rasterized=True
    )
    # cb = f.colorbar(cax)
    ax.xaxis.set_major_formatter(TimeFormatter(hop_length=1024, sr=rate))
    ax.xaxis.set_label_text('Seconds')
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_label_text('Hz')

    f.set_tight_layout(True)
    f.savefig(
        "warped.pdf",
        rasterized=True,
        bbox_inches='tight',
        dpi=300
    )

    """
    Warped Filtered
    ########################################################################
    """

    warped_audio, rate = sf.read("files/vocals_warped_filtered.wav")
    warped_audio = np.mean(warped_audio, axis=1)

    S_ref = stft(warped_audio, rate, n_fft=4096, hop_length=1024).T

    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)  # create an axes object in the figure
    ax.pcolormesh(
        x_axis, y_axis, np.log(S_ref[:, :reduce_bins].T + 0.5), cmap='gray_r', rasterized=True
    )
    # cb = f.colorbar(cax)
    ax.xaxis.set_major_formatter(TimeFormatter(hop_length=1024, sr=rate))
    ax.xaxis.set_label_text('Seconds')
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_label_text('Hz')

    f.set_tight_layout(True)
    f.savefig(
        "warped_filered.pdf",
        rasterized=True,
        bbox_inches='tight',
        dpi=300
    )

    """
    REF
    ########################################################################
    """

    warped_ref, rate = sf.read("files/vocals_ref.wav")
    warped_ref = np.mean(warped_ref, axis=1)

    S_warped = stft(warped_ref, rate, n_fft=4096, hop_length=1024).T

    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)  # create an axes object in the figure
    ax.pcolormesh(
        x_axis, y_axis, np.log(S_warped[:, :reduce_bins].T + 0.5), cmap='gray_r', rasterized=True
    )
    # cb = f.colorbar(cax)
    ax.xaxis.set_major_formatter(TimeFormatter(hop_length=1024, sr=rate))
    ax.xaxis.set_label_text('Seconds')
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_label_text('Hz')

    f.set_tight_layout(True)
    f.savefig(
        "reference.pdf",
        rasterized=True,
        bbox_inches='tight',
        dpi=300
    )

    """
    Estimates
    ########################################################################
    """

    est_audio, rate = sf.read("files/vocals.wav")
    est_audio = np.mean(est_audio, axis=1)

    S_voc = stft(est_audio, rate, n_fft=4096, hop_length=1024).T

    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)  # create an axes object in the figure
    ax.pcolormesh(
        x_axis, y_axis, np.log(S_voc[:, :reduce_bins].T + 0.5), cmap='gray_r', rasterized=True
    )
    # cb = f.colorbar(cax)
    ax.xaxis.set_major_formatter(TimeFormatter(hop_length=1024, sr=rate))
    ax.xaxis.set_label_text('Seconds')
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_label_text('Hz')

    f.set_tight_layout(True)
    f.savefig(
        "Estimate.pdf",
        rasterized=True,
        bbox_inches='tight',
        dpi=300
    )


    """
    Melodies
    ########################################################################
    """

    M_dnn = np.load("files/melody_dnn.npy")
    M_ori = np.load("files/melody_original.npy")

    x_axis = np.arange(M_ori.shape[0])
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)  # create an axes object in the figure
    line_vad, = ax.plot(
        x_axis, M_ori, color='k', label='F0 Estimate (before VAD)'
    )
    line_dnn, = ax.plot(
        x_axis, M_dnn, color='b', label='F0 Estimate (after VAD)'
    )

    ax.legend(handles=[line_vad, line_dnn], loc=3)
    # cb = f.colorbar(cax)
    ax.xaxis.set_major_formatter(TimeFormatter(hop_length=128, sr=rate))
    ax.xaxis.set_label_text('Seconds')
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_label_text('Hz')

    f.set_tight_layout(True)
    f.savefig(
        "Melodia.pdf",
        rasterized=True,
        bbox_inches='tight',
        dpi=300
    )

    """
    Warp Contour
    ########################################################################
    """

    M_dnn = np.load("files/warp_contour.npy")

    x_axis = np.arange(M_dnn.shape[0])
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)  # create an axes object in the figure
    ax.plot(
        x_axis, M_dnn, color='k'
    )

    # cb = f.colorbar(cax)
    ax.xaxis.set_major_formatter(TimeFormatter(hop_length=1, sr=rate))
    ax.xaxis.set_label_text('Seconds')
    ax.yaxis.set_label_text('Pitch Variation')

    f.set_tight_layout(True)
    f.savefig(
        "Contour.pdf",
        rasterized=True,
        bbox_inches='tight',
        dpi=300
    )
