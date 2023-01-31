#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:11:12 2023

@author: ejgipson
"""

#%% make POSCAR file for 1Be and 1O given lattice point number
import numpy as np
import pandas as pd

strucID = np.arange(1,10,1) # strucID contains the structure ID number

repBe = 11 # repBe contains the lattice number to be replaced with Be
repO = np.array([22, 6, 21, 17, 2, 3, 19, 29, 13]).astype(int) # repO contains the lattice number to be replaced with O

old = open('POSCAR','r')
lineby = old.readlines()
old.close()
POS = pd.DataFrame(lineby[8:41])[:-1]

for i in strucID:
    ind = np.append(np.delete(np.arange(0,32,1), [(repBe - 1),(repO[strucID[i]-1]-1)], None),[(repBe - 1),(repO[strucID[i]-1]-1)])
    newPOS = POS.reindex(ind).replace({r'\n':''},regex=True)
    new = open('POSCAR_%s' % str(strucID[i]),'w')
    # Line 0 is the system ID
    new.write('GBeO_%s\n' % str(strucID[i]))
    # Line 1 is the scaling = 1.0
    new.write('1.0\n')
    # Lines 2 through 4 are the (a,b,c) lattice vectors <- copy from POSCAR
    new.write('%s' % lineby[2])
    new.write('%s' % lineby[3])
    new.write('%s' % lineby[4])
    # Line 5 is 'C  Be  O'
    new.write('    C  Be  O\n')
    # Line 6 is 3'0  1  1'
    new.write('    30  1  1\n')
    # Line 7 is 'Direct'
    new.write('Direct\n')
    # Line 8 throguh 40 contains position information for C, then Be, then O 
    newPOS.to_csv(new, header=False, index=False,sep='\t')
    new.close()