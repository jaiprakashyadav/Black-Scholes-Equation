#%%
import pandas as pd
import pandas_datareader as dr
import numpy as np
from scipy.stats import norm
%matplotlib inline
df = dr.data.get_data_yahoo('RELIANCE.NS',start='2020-12-02',end='2021-02-12')
df
print(df.columns)
df1=df['Open']
print(df1)
s=[]
for i in df1:
    s.append(i)
print(s)
t=[]
time=[]
from datetime import datetime
#datetime(year, month, day)
a = datetime(2021, 2 , 13)
for i in range(len(df1.index)):
    d= a- df1.index[i]
    time.append(df1.index[i])
    j = (d.days)/365
    t.append(j)
print(t)
print(time)
#define variables
r= 0.01
k=2052
sigma=0.30
option=[]

def blackscholes(r,s,k,t,sigma):
        d1=(np.log(s/k) + (r+sigma**2/2)*t)/(sigma*np.sqrt(t))
        d2= d1 - sigma*np.sqrt(t)
        price= s*norm.cdf(d1,0,1) - k*np.exp(-r*t)*norm.cdf(d2,0,1)
        option.append(price)
        return price

for i in range(len(df1.index)):
    print(i+1," Stock price ", s[i],"On date",df1.index[i] )
    print("option price is ",round(blackscholes(r, s[i], k, t[i], sigma),2))

#Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
 
x=s
y=t
z= option

# Creating figure
fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")
   
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.3, 
        alpha = 0.2) 
 
 
# Creating plot
sctt = ax.scatter3D(x, y, z,c=z,
                    alpha = 0.8, 
                    cmap = 'hsv', 
                    marker ='^')
 
plt.title("simple 3D scatter plot")
ax.set_xlabel('Stock price', fontweight ='bold') 
ax.set_ylabel('Time', fontweight ='bold') 
ax.set_zlabel('Option Price', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
 
 
 
# show plot
plt.show()
