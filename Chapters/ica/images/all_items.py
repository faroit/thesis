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
'axes.labelsize': 10,
'text.fontsize': 10,
'legend.fontsize': 10,
'xtick.labelsize': 8,
'ytick.labelsize': 8,
'font.family': 'normal',
'font.weight': 'light',
'text.usetex': True,
'figure.figsize': fig_size}

rcParams.update(params)
# reading the data from a csv file
df = read_csv('../data/items_anon.csv', sep=',')

df['error'] = (df['GT']-df['value'] != 0)
df['diff'] = (df['GT']-df['value'])
df['classical'] = (df['item_id'] <= 6)
error_means_grouped_by_instr = df.groupby(['GT','item_id'])['diff'].mean()
error_means_grouped_by_instr_all = df.groupby(['GT'])['diff'].mean()

#ax1 = subplot(111)
#ax1.set_xticklabels(error_means_grouped_by_instr.index)
#plt.axis([.5,6.5,0,1.1])
plt.xlabel('Item ID')
plt.ylabel('Absolute Error in Instruments')

error_means_grouped_by_instr.plot(kind='bar')
#error_means_grouped_by_instr_all.plot()

plt.autoscale(enable=False)
#schoef1 = plt.axhline(y=error_means_grouped_by_instr[1][2], xmin=.1, xmax=1)

#legend([l1,l2,l3], ['Non-Musicians', 'Musicians','All'], loc=4)
#plt.show()
savefig('all_items.pdf')