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

underestimated = df[df['diff'] > 0].count()[1]
underestimated_by_one = df[df['diff'] == 1].count()[1]

overestimated = df[df['diff'] < 0].count()[1]
both = df[df['error'] == 0 df['GT'] == 1].count()[1]

print "percent of cases underestimated"
print underestimated/436.0

print "percent of cases underestimated"
print underestimated_by_one/436.0

print "percent of cases overestimated"
print overestimated/436.0
