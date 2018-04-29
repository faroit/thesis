import modules.mstft as mstft
import pylab as plt
import numpy as np
import itertools
import soundfile as sf
import argparse
import yaml
import seaborn as sns
import matplotlib as mpl


"""-------------------------------------------------------------------------------------------------
Modulation NMF, model with

each source modulation spectrogram Vj(a,b,f,t) modeled as
Vj(a,b,f,t,c) = P(a,b,f,j)At(t,j)Ac(c,j)

So we have one modulation "shape" for each frequency, hence P(a,b,f,j)
which is activated over time, this is At(t,j)  and over channels, this is
Ac(c,j)

-------------------------------------------------------------------------------------------------
Antoine Liutkus, Inria 2014"""


def displaySTFT(X, name=None):
    # display a modulation spectrogram, of shape (w1,w2,f,t)
    plt.rc('text', usetex=True)
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['text.latex.unicode'] = 'True'

    sns.set()
    sns.set_context("paper")
    sns.set_style(
        "white", {
            "grid.color": '.9',
            "font.family":
            "serif", 'font.serif':
            'ptmrr8re'
        }
    )

    params = {'backend': 'ps',
              'axes.labelsize': 14,
              'font.size': 14,
              'legend.fontsize': 12,
              'xtick.labelsize': 12,
              'ytick.labelsize': 12,
              'text.usetex': True,
              'font.family': 'serif',
              'font.serif': 'ptmrr8re',
              }

    plt.rcParams.update(params)

    fig, ax = plt.subplots(1, 1)
    plt.figure(1)
    plt.pcolormesh(
        np.flipud(abs(np.squeeze(X))),
        vmin=0,
        vmax=10,
        cmap='cubehelix_r',
    )
    plt.axis((0, 240, 0, 352))
    fig.tight_layout()
    fig.savefig(name, bbox_inches='tight', dpi=300)


def displayMSTFT(Z, name=None):
    # display a modulation spectrogram, of shape (w1,w2,f,t)
    plt.figure(1)
    (nF, nT) = Z.shape[2:4]
    for (f, t) in itertools.product(range(nF), range(nT)):
        plt.subplot(nF, nT, (nF-f-1) * nT+t+1)
        plt.pcolormesh(
            np.flipud(abs(Z[..., f, t])) ** 0.3,
            vmin=0,
            vmax=10,
            cmap='cubehelix_r',
        )
        plt.axis((0, 48, 4, 28))
        plt.xticks([])
        plt.xlabel('')
        plt.yticks([])
        plt.ylabel('')

    f = plt.gcf()
    f.subplots_adjust(wspace=0, hspace=0)

    if name is None:
        plt.show()
    else:
        plt.savefig(name)


def process(
        signal,
        rate,
        pref,
        verbose=False,
        cluster=None,
        display=True,
        save=True
):
    '''Applies CFM Separation

    Args:
       signal (ndarray):    Single or multichannel audio signal
       rate (float):        sample rate
       pref (object):       Preference object

    Returns:
       output (ndarray):    output array separated into pref.k components or
                            clustered into pref.s components using kmeans

    '''
    W = (pref['W_A'], pref['W_B'])
    mhop = (pref['mhop_A'], pref['mhop_B'])

    print 'computing STFT'
    xstft = mstft.stft(xwave, pref['nfft'], pref['thop'])
    print xstft.shape

    xstft = xstft[:384-32, 16:256]
    print xstft.shape

    # compute modulation STFT
    print 'computing modulation STFT'
    x = mstft.stft(xstft, W, mhop, real=False)
    # m = mstft.stft(np.abs(xstft), W, mhop, real=False)
    g = mstft.split(xstft, W, mhop, False, verbose)

    print 'getting modulation spectrogram, shape:', x.shape
    z = np.abs(x) ** pref['alpha']

    if save:
        np.savez_compressed('gridstft.npz', g[..., :, :, 0])
        np.savez_compressed('cft.npz', x[..., :, :, 0])

    if display:
        displaySTFT(xstft, 'out2.pdf')
        displayMSTFT(g[..., :, :, 0], 'out1.png')
        # displayMSTFT(m[..., :, :, 0], 'out2.pdf')
        displayMSTFT(z[..., :, :, 0], 'out3.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Source Separation based on Common Fate Model')

    parser.add_argument('input', type=str, help='Input Audio File')

    args = parser.parse_args()

    # Parsing settings
    with open("settings.yml", 'r') as f:
        doc = yaml.load(f)

    pref = doc['general']

    filename = args.input

    # loading signal
    (xwave, fs) = sf.read(filename)

    out = process(xwave, fs, pref)
