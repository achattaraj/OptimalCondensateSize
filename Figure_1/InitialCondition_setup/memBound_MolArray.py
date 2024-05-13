# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:58:40 2023

@author: chatt
"""

import numpy as np 
from random import sample 

def writeDataFile(seq=[1,2]*3, typName={}, 
                  NumMol=10, xLim=(-200,200), yLim=(-200,200)):
    '''
    seq: sequence of atoms within a molecule
    typName: atom types within a molecule
    '''
    N_atom = len(seq)
    N_tot = NumMol * N_atom
    xl, xh = xLim[0], xLim[1]
    yl, yh = yLim[0], yLim[1]
    
    xyz_file = f'N{NumMol}_Nephrin.xyz'
    
    with open(xyz_file, 'w') as xf:
        xf.write(f'\t\t{N_tot}\n')
        xf.write(' To be merged with Packmol  \n')
        
        x = sample(range(xl,xh), NumMol)
        y = sample(range(xl,xh), NumMol)
        xy_coor = list(zip(x,y))
        
        for i in range(NumMol):
            z = 5 
            x, y = xy_coor[i]
            for j in range(N_atom):
                xf.write(f'{typName[seq[j]]}\t\t{x} {y} {z}\n')
                z += 10

    


seq = [3,2,2,1,2,2,1,2,2,1]
typName = {3:'Anchor', 2:'NephL', 1:'pY'}
# 3: anchor, 2: nephL, 1: pY
xLim = (-230, 230)
yLim = (-230, 230)
writeDataFile(seq=seq, typName=typName, NumMol=80, xLim=xLim, yLim=yLim)    
   