#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:45:30 2021

@author: ejgipson
"""
#%% DENSITY OF STATES
import pandas as pd
import matplotlib.pyplot as plt

file = open('/Users/ejgipson/Desktop/Spring_23/00-THESIS/01-DATA/06-O/02/DOSCAR')

lst = []
for line in file:
    lst += [line.split()]

struc_info = lst[5]
EMAX = float(struc_info[0])
EMIN = float(struc_info[1])
NEDOS = int(struc_info[2])
EFERMI = float(struc_info[3])

temp = lst[6:]

#### TDOS ####
DOS = [x for x in temp if len(x)==3]
DOS = pd.DataFrame(DOS).astype(float)
DOSMAX = DOS[1].max()

#### spd DOS ####
spdDOS = [x for x in temp if len(x)==10]
spdDOS = pd.DataFrame(spdDOS).astype(float)
n = len(spdDOS) - NEDOS
spdDOS = spdDOS.iloc[n:,:]
sDOS = pd.DataFrame(spdDOS[1])
pDOS = pd.DataFrame(spdDOS[2] + spdDOS[3] + spdDOS[4])

Tfont = {'fontname':'Times'}
fig, ax = plt.subplots(dpi=1200)
plt.plot(DOS[0],DOS[1],'k',linewidth=1.0)
plt.xlabel('E (eV)',**Tfont)
plt.ylabel('DOS',**Tfont)
ax.yaxis.set_label_coords(-0.01,0.5)
plt.yticks(color='w')
plt.xticks(**Tfont)
plt.axis([EMIN,EMAX,0.1,(DOSMAX+1)])
plt.vlines(EFERMI,0,(DOSMAX+1),colors='red',linestyle='dashed',linewidth=0.5)
ax.spines[['right','top']].set_visible(False)
ax.grid()
#%% BAND STRUCTURE DIAGRAM
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

EIG = open('/Users/ejgipson/Desktop/Spring_23/00-THESIS/01-DATA/05-Be/08/EIGENVAL')
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
    k = temp.loc[temp[0] == i+1]
    plt.plot(path,k[1],color='k',linewidth=0.75)
   
#### Adding a dashed line for Fermi Level ####
DOS = open('/Users/ejgipson/Desktop/Spring_23/00-THESIS/01-DATA/06-O/02/DOSCAR')
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