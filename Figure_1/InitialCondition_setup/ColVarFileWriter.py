# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:03:12 2024

@author: chatt
"""

import numpy as np

# middle beads of cytosolic proteins (Nck, NWASP, Arp)

nck_Id = np.arange(5, 240+5, 10) + 800
nw_Id = np.arange(10, 120+10, 10) + 3200
arp_Id = np.arange(2,120+2,3) + 5480

Idx_grp1 = np.concatenate((nck_Id, nw_Id, arp_Id))

# anchor beads of nephrin 
Idx_grp2 = np.arange(1, 801, 10)


with open('FromMemDist.colvars', 'w') as tmf:
    tmf.writelines('colvarsTrajFrequency 50000\n')
    tmf.writelines('colvarsRestartFrequency 50000\n\n')
    tmf.writelines('colvar {\n')
    tmf.writelines('\tname dist\n')
    tmf.writelines('\tlowerBoundary 0.0\n')
    tmf.writelines('\tupperBoundary 205.0\n\n')
    tmf.writelines('distance {\n')
    tmf.writelines('\t\tgroup1 { \n\t\t\tatomNumbers ')
    for a1 in Idx_grp1:
        tmf.writelines(f'{a1}\t')
    tmf.writelines('\n\t\t\t}\n\n')
    
    tmf.writelines('\t\tgroup2 { \n\t\t\tatomNumbers ')
    for a2 in Idx_grp2:
        tmf.writelines(f'{a2}\t')
        
    tmf.writelines('\n\t\t\t}\n')
    tmf.writelines('\t\t}\n')
    tmf.writelines('\t}\n\n')
    
    tmf.writelines('metadynamics {\n')
    tmf.writelines('\tname MtD_dist\n')
    tmf.writelines('\tcolvars dist\n')
    tmf.writelines('\thillWeight 0.2 \n')
    tmf.writelines('\tnewHillFrequency 500\n')
    tmf.writelines('\tdumpFreeEnergyFile yes\n')
    tmf.writelines('\twriteHillsTrajectory on \n')
    tmf.writelines('\thillwidth 1.0 \n')
    tmf.writelines('\twellTempered on \n')
    tmf.writelines('\tbiasTemperature 310 }\n\n')
    
    tmf.writelines('harmonicWalls {\n')
    tmf.writelines('\tname wall_dist\n')
    tmf.writelines('\tcolvars dist\n')
    tmf.writelines('\tupperWalls 198\n')
    tmf.writelines('\tupperWallConstant 20.0 }\n')
    


