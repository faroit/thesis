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

listening = df[df['familiar_listening_tests'] == 0]['diff']
nlistening = df[df['familiar_listening_tests'] == 1]['diff']
classic = df[df['item_id'] < 7]['diff']
non_classic = df[df['item_id'] >= 7]['diff']

w_val_diff, p_val_diff = stats.levene(classic, non_classic)
w_val_diff2, p_val_error2 = stats.levene(listening, nlistening)

print "p value of levene test for diff classic/non-classic:"
print p_val_diff

print "p value of levene test for diff fam_listening/nfam test:"
print p_val_error2

print "mean diff of items from classical genre"
print np.around(classic.mean(),decimals=2)

print "mean diff of items from non-classical genre"
print np.around(non_classic.mean(),decimals=2)

print "variance of diff of items from classical genre"
print np.around(classic.var(),decimals=2)

print "variance of diff of items from non-classical genre"
print np.around(non_classic.var(),decimals=2)