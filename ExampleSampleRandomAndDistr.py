

#########################
# Short code to select a speaker at random
# date:
# Developer:
# Requirements:
import numpy as np
import pandas as pd
# python3
# numpy
# names of names_speakers - hard coded
#########################
names_speakers = { 1:'j', 2:'s', 3:'a'} #https://docs.python.org/3.6/tutorial/datastructures.html
x = np.random.rand()
print(int( np.ceil(3*x) ))
print(names_speakers[ int( np.ceil(3*x) ) ] )
#########################
# Demonstrate it working
for j in range(5):
    x = np.random.rand()
    print(int( np.ceil(3*x) ))
    print(names_speakers[ int( np.ceil(3*x) ) ] )
#########################
# Demonstrate something else
N = 20*1000
# https://en.wikipedia.org/wiki/Gamma_distribution
x2 = np.random.gamma(2,10,N)
df = pd.DataFrame(x2,columns=['Distr'])#,index=data[:,0]),
print(df.head())
print(df.Distr.hist(bins=int(N/1000))) # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
#########################
