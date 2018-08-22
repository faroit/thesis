import matplotlib.pyplot as plt
import os
from pylab import *
from scipy import stats  

from pandas import read_csv
from pandas.tools import plotting
import numpy as np

# reading the data from a csv file
df = read_csv('../data/items_anon.csv', sep=',')

df['error'] = (df['GT']-df['value'] != 0)
df['diff'] = (df['GT']-df['value'])
df['adiff'] = abs(df['GT']-df['value'])

Summed = df.groupby(['GT','item_id','musical','value'])['value'].count().unstack()

instrument1 = df[df['GT'] == 1]['error']
instrument2 = df[df['GT'] == 2]['error']
instrument3 = df[df['GT'] == 3]['error']
instrument4 = df[df['GT'] == 4]['error']
instrument5 = df[df['GT'] == 5]['error']
instrument6 = df[df['GT'] == 6]['error']

f_val, p_val = stats.f_oneway(instrument1, instrument2, instrument3, instrument4, instrument5, instrument6)

print p_val