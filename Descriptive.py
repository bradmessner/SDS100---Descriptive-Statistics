# ***********************************************
# * Name:   Basic Statistics in Python
# * Date:   Feb 20, 2022
# * Ver:    Python 2.7, 3.10
# * Author: Brad D. Messner
# * Desc:   Importing a file and calculating basic
# *         descriptive analytics.
# ***********************************************

import pandas as pd
import statistics
import numpy as np

df = pd.read_csv("/Users/bradmessner/Desktop/MELBOURNE_HOUSE_PRICES_LESS.csv")
# print df.head()     # prints the first 5 lines of your data file
df.info()           # outputs the basic info about my data


df = df.dropna(subset=['Price'])
myData = df['Price'].tolist()

print(myData)
print("Count is:  ", len(myData))
print("Mean is:   ", statistics.mean(myData))
print("Median is: ", statistics.median(myData))
print("Mode is:   ", statistics.mode(myData))
print("Min is:    ", min(myData))
print("Max is:    ", max(myData))
print("Range is:  ", max(myData)-min(myData))
print("St Dev is: ", statistics.stdev(myData))
print("Variance:  ", statistics.variance(myData))
print("Lower Q:   ", np.percentile(myData, 25))
print("Upper Q:   ", np.percentile(myData, 75))
print("Inter Q R: ", np.percentile(myData, 75) - np.percentile(myData, 25))
