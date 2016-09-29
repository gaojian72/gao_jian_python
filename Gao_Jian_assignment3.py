# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:34:46 2016

@author: Jian Gao
Group C
"""

import urllib
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plot
import numpy as np

# Question 1
'''
Search for the IRIS dataset on the internet. You should quickly find the UCI Machine
Learning repository. Instead of downloading the files, figure out how to directly load the files
from the internet into Python and add the column names using Python code instead of an editor.
'''

iris_name='http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names'
iris_data='http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

column=['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

data=pd.read_csv(iris_data, names=column)

# Question 2
'''
Using Pandas, display the first ten and last ten rews of the data.
'''
data.head(10)
data.tail(10)

# Question 3
'''
Using Pandas, print simple location statistics(Count, Mean, STD, Min, 25%, 50%,
75%, MAX).
'''
data.describe()

# Question 4
def plothist(x):
   '''
   Write a function that accepts a list of numbers that represent numbers of bins and
   using Pandas, plots a histogram for each of the numberic columns at each bin size.
   Parameter:
   a list of data of bin sizes
   Returns:
   histograms 
   '''
   for col in column[0:4]:
        for i in x:
            data.hist(column=col, bins=i)
plothist([10,50,100])

# Question 5
'''
Plot a box plot for each of the numeric column.
'''
for i in column[0:4]:
    plot.figure()
    # create a new figure
    data[i].plot.box()
    # box plot

# Question 6
'''
Plot a bar chart for the nominal column.
'''
plot.figure('sepal length bar')# create a new figure
data['sepal length'].plot.bar()# box plot
plot.figure('sepal width bar')
data['sepal width'].plot.bar()
plot.figure('petal length bar')
data['petal length'].plot.bar()
plot.figure('petal width bar')
data['petal width'].plot.bar()

####### another version ############           
for i in column[0:4]:
    plot.figure()
    # create a new figure
    data[i].plot.bar()
    # bar plot        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        











