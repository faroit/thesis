import matplotlib.pyplot as plt
import os
from pylab import *

import numpy as np
import matplotlib.colors as acolors

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
r = np.genfromtxt("../data/group_comparison_mn.csv",delimiter='\t',dtype=None)

Mus 	= np.zeros((12,12))
NMus 	= np.zeros((12,12))
MusNMus = np.zeros((12,12))

for x in arange(0,12,2):
	for y in arange(0,12,2):
		if r[x,y] < 0.05:
			NMus[x,y] = 20*r[x,y]
		else:
			NMus[x,y] = 1

for x in arange(1,12,2):
	for y in arange(1,12,2):
		if r[x,y] < 0.05:
			Mus[x,y] = 20*r[x,y]
		else:
			Mus[x,y] = 1

for x in arange(0,12,2):
	for y in arange(1,12,2):
		if r[x,y] < 0.05:
			Mus[x,y] = 20*r[x,y]
			NMus[x,y] = 20*r[x,y]
		else:
			Mus[x,y] = 1
			NMus[x,y] = 1
	
for x in arange(1,12,2):
	for y in arange(0,12,2):
		if r[x,y] < 0.05:
			Mus[x,y] = 20*r[x,y]
			NMus[x,y] = 20*r[x,y]
		else:
			Mus[x,y] = 1
			NMus[x,y] = 1
	



rgb = np.dstack([Mus,NMus,MusNMus])

#(can also take RGB values, like (255,255,255):

cdict = {'green': ((0.0, 0.0, 0.0),
                 (0.05, 0.0, 0.0),
                 (1.0, 0.0, 1.0)),
         'red': ((0.0, 0.0, 0.0),
                   (0.05, 1, 1),
                   (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),
                  (0.05, 0.0, 0.0),
                  (1.0, 0.0, 1.0))}

new_map = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)

plt.figure()
ax = subplot(1,1,1)

x = arange(0,13)
y = arange(0,13)
ax.set_xlabel('Instruments')
ax.set_ylabel('Instruments')

#pcolor(x,y,r, cmap=new_map)

# make a color map of fixed colors
cmap = acolors.ListedColormap(['white', 'red'])
bounds=[0,5,10]
norm = acolors.BoundaryNorm(bounds, cmap.N)

plt.imshow(rgb,interpolation='nearest', origin='lower',cmap=cmap, norm=norm,extent=[0,6,0,6])

ax.set_xlim([0,6])
ax.set_ylim([0,6])

xticks( arange(0,6), ('1', '2', '3', '4', '5', '6') )
yticks( arange(0,6), ('1', '2', '3', '4', '5', '6') )

ax.grid(which='major', linestyle='-', color='white') 

ax.xaxis.grid(True)
ax.yaxis.grid(True)

l1 = Line2D([], [], linewidth=3, color="g") 
l2 = Line2D([], [], linewidth=3, color="r") 
l3 = Line2D([], [], linewidth=3, color="y") 

plt.legend([l1, l2, l3], ["Musicians", "Non-Musicians", "Interaction"],loc='lower right')
savefig('comparison.pdf')
#show()
