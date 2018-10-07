import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
plt.rcParams['legend.fancybox'] = True

import os
from pylab import *

from pandas import read_csv
from pandas.tools import plotting
import numpy as np

def fill_between2(x, y1, y2=0, ax=None, **kwargs):
    """Plot filled region between `y1` and `y2`.

    This function works exactly the same as matplotlib's fill_between, except
    that it also plots a proxy artist (specifically, a rectangle of 0 size)
    so that it can be added it appears on a legend.
    """
    ax = ax if ax is not None else plt.gca()
    ax.fill_between(x, y1, y2, **kwargs)
    p = plt.Rectangle((0, 0), 0, 0, **kwargs)
    ax.add_patch(p)
    return p

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin'

fig_width_pt = 600  # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72               # Convert pt to inch
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = fig_width*golden_mean      # height in inches
fig_size =  [fig_width,fig_height]

params = {
'axes.labelsize': 16,
'text.fontsize': 16,
'legend.fontsize': 14,
'xtick.labelsize': 14,
'ytick.labelsize': 14,
'font.family': 'normal',
'font.weight': 'normal',
'text.usetex': True,
'figure.figsize': fig_size}

rcParams.update(params)
# reading the data from a csv file
df = read_csv('../data/items_anon.csv', sep=',')

df['error'] = (df['GT']-df['value'] != 0)
df['classical'] = (df['item_id'] <= 6)

grouped_certainty_in_percent = df.groupby(['GT','certainty'])['certainty'].count().unstack()*100/124
plt.figure()

ax = subplot(1,1,1)

certainty_array = np.array(grouped_certainty_in_percent)
certainty_array_t = certainty_array.transpose()
certainty_array_t = np.flipud(certainty_array_t)
y_stack = np.cumsum(certainty_array_t, axis=0)
x = arange(1,7)
ax.set_xlabel('Number of Instruments')
ax.set_ylabel('Cumulative Certainty in Percent')
#plt.title('Overall Error')
width = 1

p1 = plt.bar(x, certainty_array_t[0], width, facecolor=(0.02, 0.21, 0.52), label="uncertain")
p2 = plt.bar(x, certainty_array_t[1], width, facecolor=(0.33, 0.46, 0.61), bottom=certainty_array_t[0], label="certain")
p3 = plt.bar(x, certainty_array_t[2], width, facecolor=(0.74, 0.78, 0.85), bottom=certainty_array_t[1]+certainty_array_t[0],label="very certain")

#p1 = fill_between2(x, 0, y_stack[0,:], label="uncertain", facecolor='1', alpha=1, hatch='---')
#p2 = fill_between2(x, y_stack[0,:], y_stack[1,:],facecolor='0.9', alpha=1, hatch='///', label="certain")
#p3 = fill_between2(x, y_stack[1,:], y_stack[2,:], facecolor='0.8', alpha=1, hatch='...', label="very certain")

pad = 0
for i in np.arange(0,6):
	ax.text(i+1.35, y_stack[0,i]-certainty_array_t[0,i]/2-1, "%s%s" % (np.around(certainty_array_t[0,i],decimals=2), "%"), size=10, color='w', backgroundcolor=(0.02, 0.21, 0.52))
	ax.text(i+1.35, y_stack[1,i]-certainty_array_t[1,i]/2-2, "%s%s" % (np.around(certainty_array_t[1,i],decimals=2), "%"), size=10, color='w', backgroundcolor=(0.33, 0.46, 0.61))
	ax.text(i+1.35, y_stack[2,i]-certainty_array_t[2,i]/2-2, "%s%s" % (np.around(certainty_array_t[2,i],decimals=2), "%"), size=10, backgroundcolor=(0.74, 0.78, 0.85))

ax.set_xlim([1,7])
ax.set_ylim([0,100])
plt.xticks(x+0.5, ('1', '2', '3', '4', '5', '6') )

plt.legend([p3,p2,p1], ["uncertain", "certain", "very certain"], loc=2, bbox_to_anchor=(1.05, 1),  borderaxespad=0.)
savefig('certainty.pdf', bbox_inches='tight')
#show()
