"""
@author VRAJ PATEL (20CE111)

"""
"""
Write a procedure to find min, max, mean, standard deviation, variance of number list.
Example
Input : 10 50 80 70 49 23 11 4
output : 4 80 37.13 27.25 848.70"""
from re import A
import statistics
import pandas as pd
a=list(map(int,input().split(' ')))
sr = pd.Series(a)
mean = sr.mean()
median = sr.median()
mode = sr.mode()
stdeviation = sr.std(axis=0, skipna=True)
print(sr.min(),' ',sr.max(),' ',mean,' ',stdeviation,' ',statistics.variance(sr))

