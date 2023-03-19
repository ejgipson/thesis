#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:45:30 2023

@author: ejgipson
"""
#%% BAND STRUCTURE DIAGRAM
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

EIG = open('[path]/EIGENVAL')
lst = []
for line in EIG:
    lst += [line.split()]
        
EIG_info = lst[5] # [no. electrons, no. k points in path, no. bands]

#### Plot Band Structure ####
fig, ax = plt.subplots(dpi=1200)
path = np.arange(0,int(EIG_info[1]))

temp = [x for x in lst if len(x)==3]
temp = pd.DataFrame(temp)
temp = temp.iloc[1:,:]
temp = temp.astype(float)

for i in range(0,int(EIG_info[2])-1):
    k = temp.loc[temp[0] == i+1] # From temp, send every row with column zero value matching i+1 to k
    plt.plot(path,k[1],color='k',linewidth=0.75) # Plot, band i against path
   
#### Adding a dashed line for Fermi Level ####
DOS = open('[path]/DOSCAR')
lst = []
for line in DOS:
    lst += [line.split()]
DOS_info = lst[5]
EFERMI = float(DOS_info[3])
plt.axhline(y=EFERMI,color='r',linestyle='--',linewidth=0.75, dashes=(7.5, 5))

#### Plot with features ####
Tfont = {'fontname':'Times'}
plt.axvline(x=0,color='k',linewidth=1)
plt.axvline(x=29,color='k',linewidth=1)
plt.axvline(x=59,color='k',linewidth=1)
plt.axvline(x=89,color='k',linewidth=1)
plt.axvline(x=119,color='k',linewidth=1)
plt.axvline(x=149,color='k',linewidth=1)
plt.axvline(x=179,color='k',linewidth=1)
plt.xlim([0,89])
plt.xticks([0,29,59,89,119,149,179],["$\Gamma$","M","K","$\Gamma$","M","K'","$\Gamma$"],**Tfont)
plt.yticks(**Tfont)
plt.ylabel('Energy (eV)',**Tfont)
plt.xlabel('Wave Vector',**Tfont)
plt.ylim(EFERMI-4,EFERMI+4)
plt.grid()
plt.title('')
plt.show()
