import matplotlib.pyplot as plt
import os
from pylab import *

from pandas import read_csv
from pandas.tools import plotting
import numpy as np

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin'

fig_width_pt = 600  # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72               # Convert pt to inch
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = fig_width*golden_mean      # height in inches
fig_size =  [fig_width,fig_height]

params = {
'axes.labelsize': 12,
'text.fontsize': 12,
'legend.fontsize': 12,
'xtick.labelsize': 8,
'ytick.labelsize': 8,
'font.family': 'normal',
'font.weight': 'normal',
'text.usetex': True,
'figure.figsize': fig_size}

rcParams.update(params)
# reading the data from a csv file
df = read_csv('../data/items_anon.csv', sep=',')

df['error'] = (df['GT']-df['value'] != 0)

error_means_grouped_by_instr = df.groupby(['GT','musical'])['error'].var().unstack()
error_means_grouped_by_instr[3] = df.groupby(['GT'])['error'].var()

fig = plt.figure()

ax1 = subplot(111)
ax1.set_xticklabels(error_means_grouped_by_instr.index)

ax1.set_xlim([1,6])
ax1.set_ylim([0,1.05])
ax1.set_xlabel('Number of Instruments')
ax1.set_ylabel('Error probability')
l1,l2,l3 = ax1.plot(
	error_means_grouped_by_instr.index,error_means_grouped_by_instr[0],'r^-',
	error_means_grouped_by_instr.index,error_means_grouped_by_instr[1],'go-',
	error_means_grouped_by_instr.index,error_means_grouped_by_instr[3],'b--')

ax1.autoscale(enable=False)
#schoef1 = plt.axhline(y=error_means_grouped_by_instr[1][2], xmin=.1, xmax=1)

ax1.legend([l1,l2,l3], ['Non-Musicians', 'Musicians','All'], loc=4)
#plt.show()
savefig('error_var.pdf')