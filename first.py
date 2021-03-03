#%%
import numpy as np
from scipy.stats import norm

#define variables
r= 0.01
s = []
for i in range(1,40):
    s.append(i)
k=40
t=[]
for i in range(1,365):
    t.append(i/365)
sigma=0.30

def blackscholes(r,s,k,t,sigma):
  d1=(np.log(s[i]/k) + (r+sigma**2/2)*t[j])/(sigma*np.sqrt(t[j]))
  d2= d1 - sigma*np.sqrt(t[j])
  price= s[i]*norm.cdf(d1,0,1) - k*np.exp(-r*t[j])*norm.cdf(d2,0,1)
  return price

for i in range(1,39):
    for j in range(1,364):
        print("option price for stock price ",s[i],"and time ",t[j],round(blackscholes(r, s, k, t, sigma),2))

# %%
