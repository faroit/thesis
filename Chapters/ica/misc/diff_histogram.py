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

df['diff'].hist()
show()
