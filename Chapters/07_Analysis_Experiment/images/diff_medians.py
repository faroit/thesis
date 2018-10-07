import matplotlib.pyplot as plt
plt.rcParams['legend.fancybox'] = True
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
'axes.labelsize': 18,
'text.fontsize': 18,
'legend.fontsize': 18,
'xtick.labelsize': 14,
'ytick.labelsize': 14,
'font.family': 'normal',
'font.weight': 'light',
'text.usetex': True,
'figure.figsize': fig_size}

rcParams.update(params)
# reading the data from a csv file
df = read_csv('../data/items_anon.csv', sep=',')

df['error'] = (df['GT']-df['value'] != 0)
df['diff'] = (df['GT']-df['value'])

error_means_grouped_by_instr = df.groupby(['GT','musical'])['diff'].median().unstack()
error_means_grouped_by_instr[3] = df.groupby(['GT'])['diff'].median()

fig = plt.figure()
ind = np.arange(1,7)  # the x locations for the groups

width = 0.35       # the width of the bars

ax1 = subplot(111)

ax1.set_xlim([0.8,7])
ax1.set_ylim([-0.2,3.25])

ax1.set_xticks(ind+width+0.05)
ax1.set_xticklabels( ('1', '2', '3', '4', '5', '6') )

ax1.set_xlabel('Number of Instruments')
ax1.set_ylabel('Median($\Delta_I = I-R$)')
#plt.title('Overall Error')
l1 = ax1.bar(error_means_grouped_by_instr.index,error_means_grouped_by_instr[0], width/2, color='m', hatch='...')
l3 = ax1.bar(error_means_grouped_by_instr.index+width/2+0.05,error_means_grouped_by_instr[3], width, color='1', hatch='///')
l2 = ax1.bar(error_means_grouped_by_instr.index+(width*1.5)+0.1,error_means_grouped_by_instr[1], width/2,color='c')

ax1.autoscale(enable=False)
#schoef1 = plt.axhline(y=error_means_grouped_by_instr[1][2], xmin=.1, xmax=1)

ax1.legend([l1,l2,l3], ['Non-Musicians', 'Musicians', 'All'], loc=2)
#plt.show()
savefig('diff_medians.pdf')