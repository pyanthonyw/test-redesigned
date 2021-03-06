

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
names_speakers = { 1:'JC', 2:'SH', 3:'AW', 4:'SW'} #https://docs.python.org/3.6/tutorial/datastructures.html
np.random.seed(62)
x = np.random.rand()
print(int( np.ceil(len(names_speakers)*x) ))
print(names_speakers[ int( np.ceil(len(names_speakers)*x) ) ] )
#########################
# Demonstrate it working
for j in range(5):
    x = np.random.rand()
    print(int( np.ceil(len(names_speakers)*x) ))
    print(names_speakers[ int( np.ceil(len(names_speakers)*x) ) ] )



#X = np.random.beta(2,10)

#########################
# Demonstrate something else New
N = 20*1000
# https://en.wikipedia.org/wiki/Gamma_distribution
x2 = np.random.gamma(2,10,N)
df = pd.DataFrame(x2,columns=['Distr'])#,index=data[:,0]),
print(df.head())

# Useful
print(df.Distr.hist(bins=int(N/1000))) # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
# Also Useful
print(df.Distr.hist(bins=int(N/100))) # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
# Danger
print(df.Distr.hist(bins=int(N/10))) # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
#########################

#########################
