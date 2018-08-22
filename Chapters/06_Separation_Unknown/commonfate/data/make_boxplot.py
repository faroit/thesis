import numpy as np
import matplotlib.pyplot as plt
import argparse
import math
import pandas as pd
import seaborn as sns
import matplotlib as mpl
from scipy.io import loadmat
from matplotlib.transforms import BlendedGenericTransform


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Perform pitch estimation for given sensor data file.')
    parser.add_argument(dest='input', type=str, default=None)

    parser.add_argument(dest='output', type=str, default=None,
                        help='pdf')

    args = parser.parse_args()

    df = pd.read_pickle(args.input)

    # only plot the results for k == 2
    df = df.query('k == 2')

    mat = loadmat('data/score_HRNMF.mat')

    # adding results for HRNMF for Qa=1
    df_mat = pd.DataFrame(
        mat['score_HRNMF']['SDR'][0][0][:, 0], columns=['SDR']
    )
    df_mat['SIR'] = pd.DataFrame(
        mat['score_HRNMF']['SIR'][0][0][:, 0], columns=['SIR']
    )
    df_mat['SAR'] = pd.DataFrame(
        mat['score_HRNMF']['SAR'][0][0][:, 0], columns=['SAR']
    )
    df_mat['method'] = 'HRNMF'
    df_mat['k'] = 2

    df = df.append(df_mat, ignore_index=True)

    df.method = df.method.str.upper()

    # reshape data
    # df = pd.melt(
    #    df, id_vars=['method'], value_vars=['SDR', 'SAR', 'SIR'],
    #    var_name='measure', value_name='score'
    # )

    plt.rc('text', usetex=True)

    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['text.latex.unicode'] = 'True'

    sns.set()
    sns.set_context("paper")
    sns.set_style(
        "white", {
            "font.family":
            "serif", 'font.serif':
            'ptmrr8re'
        }
    )

    fig_width_pt = 244.6937  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0 / 72.27               # Convert pt to inch
    golden_mean = (math.sqrt(5) - 1.0) / 2.0         # Aesthetic ratio
    fig_width = fig_width_pt * inches_per_pt  # width in inches
    fig_height = fig_width * golden_mean      # height in inches
    fig_size = np.array([fig_width*2.5, fig_height*1.5])

    params = {'backend': 'ps',
              'axes.labelsize': 14,
              'font.size': 14,
              'legend.fontsize': 12,
              'xtick.labelsize': 12,
              'ytick.labelsize': 12,
              'text.usetex': True,
              'font.family': 'serif',
              'font.serif': 'ptmrr8re',
              'figure.figsize': fig_size}

    plt.rcParams.update(params)
    measures = ['SDR', 'SIR', 'SAR']

    f, ax = plt.subplots(1, len(measures), figsize=fig_size)

    meanlineprops = dict(linestyle='dotted', linewidth=1.5, color='#2E2E2E')

    for i, measure in enumerate(measures):
        sns.boxplot(
            "k",
            measure,
            hue='method',
            data=df,
            showmeans=True,
            showfliers=False,
            palette=sns.color_palette('muted'),
            ax=ax[i],
            width=1,
            meanline=True,
            meanprops=meanlineprops,
        )

    sns.despine(top=True, right=True)

    lgd = ax[1].legend(
        loc='lower center',
        bbox_to_anchor=(0.5, -0.22),
        bbox_transform=BlendedGenericTransform(f.transFigure, ax[1].transAxes),
        ncol=6
    )

    ax[0].legend_ = None
    ax[2].legend_ = None

    ax[0].get_xaxis().set_ticks([])
    ax[0].set_xlabel('')
    ax[1].get_xaxis().set_ticks([])
    ax[1].set_xlabel('')
    ax[2].get_xaxis().set_ticks([])
    ax[2].set_xlabel('')
    f.set_tight_layout(True)
    f.savefig(
        args.output,
        bbox_inches='tight',
        bbox_extra_artists=(lgd,),
        dpi=300
    )
