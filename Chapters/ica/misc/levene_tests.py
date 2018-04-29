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
df['adiff_asin'] = np.arcsin(np.sqrt(df['adiff'])/max(df['adiff']))

instrument1error = df[df['GT'] == 1]['error']
instrument2error = df[df['GT'] == 2]['error']
instrument3error = df[df['GT'] == 3]['error']
instrument4error = df[df['GT'] == 4]['error']
instrument5error = df[df['GT'] == 5]['error']
instrument6error = df[df['GT'] == 6]['error']

instrument1diff = df[df['GT'] == 1]['adiff']
instrument2diff = df[df['GT'] == 2]['adiff']
instrument3diff = df[df['GT'] == 3]['adiff']
instrument4diff = df[df['GT'] == 4]['adiff']
instrument5diff = df[df['GT'] == 5]['adiff']
instrument6diff = df[df['GT'] == 6]['adiff']

instrument1diff_asin = df[df['GT'] == 1]['adiff_asin']
instrument2diff_asin = df[df['GT'] == 2]['adiff_asin']
instrument3diff_asin = df[df['GT'] == 3]['adiff_asin']
instrument4diff_asin = df[df['GT'] == 4]['adiff_asin']
instrument5diff_asin = df[df['GT'] == 5]['adiff_asin']
instrument6diff_asin = df[df['GT'] == 6]['adiff_asin']

w_val_error, p_val_error = stats.levene(instrument1error, instrument2error, instrument3error, instrument4error, instrument5error, instrument6error)

w_val_diff, p_val_diff = stats.levene(instrument1diff, instrument2diff, instrument3diff, instrument4diff, instrument5diff, instrument6diff)

w_val_diff_asin, p_val_diff_asin = stats.levene(instrument1diff_asin, instrument2diff_asin, instrument3diff_asin, instrument4diff_asin, instrument5diff_asin, instrument6diff_asin)


print "p value of levene test for var ERROR:"
print p_val_error

print "p value of levene test for var abs(DIFF):"
print p_val_diff

print "p value of levene test for asin-transformed var DIFF:"
print p_val_diff_asin