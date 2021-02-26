#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from scipy import signal
np.warnings.filterwarnings('ignore')
code_length= 8
code=[[-1,-1],[-1,1]]
[r1,c1]=np.shape(code)
while r1<code_length:
    code=np.concatenate((code,code))
    code=np.concatenate((code,code),axis=1)
    for i in range(r1):
        for j in range(c1):
            code[i+r1][j+c1]=-1*code[i][j]
    [r1, c1] = np.shape(code)
print(code)


# In[2]:


sum=0;
data=[];
rows=[];
for i in range(r1):
    A=code[i][:]
    for j in range(r1):
        B=code[j][:]
        for k in range(c1):
            sum=sum+A[k]*B[k]
        data.append(sum)
        sum=0
    count=0
    for h in range(len(data)):
        if data[h]>0:
            count=count+1
    data=[]
    if count<=1:
       rows.append(i)
if len(rows)==r1:
    print('All rows are orthgnal with each other')
else:
    print('Following given rows are orthognal with each other',str(rows))


# In[3]:


def autoCorr(x, lag):
    result = np.correlate(x, x, mode= 'full')
    return result[result.size//2:]/np.correlate(x,x)


# In[4]:


def crossCorr(row1, row2):
    result =  np.correlate(row1, row2 , 'full')
    rx = np.correlate(row1, row1)
    ry = np.correlate(row2, row2)
    result = result/((rx*ry)**0.5)
    return result


# In[ ]:


plt.figure(figsize = (50,50))
nrow_plot, ncol_plot = code.shape
lag = ncol_plot
matrix = code
for j in range(nrow_plot):
    for k in range(ncol_plot):
        plt.subplot(nrow_plot, ncol_plot, 1+j*nrow_plot+k)
        if j == k:
            ac = autoCorr(matrix[j], lag)
#             ac = mmscaler.fit_transform(np.expand_dims(ac, axis=1))
            plt.plot(ac, 'r')
            plt.plot([0,nrow_plot-1], [0,0])
        else:
            cc = crossCorr(matrix[j], matrix[k])
#             cc = mmscaler.fit_transform(np.expand_dims(cc, axis=1))
            plt.plot(cc)
            plt.plot([0,2*nrow_plot-2], [0,0])
        plt.ylim(-1,1)
plt.savefig('Correlation_Walsh_128_nu')


# In[ ]:


clean_signal = pd.DataFrame(code, dtype=float) 
# print(clean_signal)
mu, sigma = 0, 0.1 
noise = np.random.normal(mu, sigma, code.shape)
# print(noise)
signal = clean_signal + noise


# In[ ]:


plt.figure(figsize = (50,50))
nrow_plot, ncol_plot = code.shape
lag = ncol_plot
matrix = signal
for j in range(nrow_plot):
    for k in range(ncol_plot):
        plt.subplot(nrow_plot, ncol_plot, 1+j*nrow_plot+k)
        if j == k:
            ac = autoCorr(matrix[j], lag)
#             ac = mmscaler.fit_transform(np.expand_dims(ac, axis=1))
            plt.plot(ac, 'r')
            plt.plot([0,nrow_plot-1], [0,0])
        else:
            cc = crossCorr(matrix[j], matrix[k])
#             cc = mmscaler.fit_transform(np.expand_dims(cc, axis=1))
            plt.plot(cc)
            plt.plot([0,2*nrow_plot-2], [0,0])
        plt.ylim(-1,1)
plt.savefig('Correlation_Walsh_8_nu_Noise')


# In[ ]:




