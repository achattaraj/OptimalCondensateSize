# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:35:45 2023

@author: chatt
"""

import numpy as np 

def parseXYZ(file):
    with open(file, 'r') as tf:
        lines = tf.readlines()
    return lines[2:]

def mergeFiles(f1, f2, path=''):
    '''Merge two xyz files f1 & f2 '''
    l1, l2 = parseXYZ(f1), parseXYZ(f2)
    fName = 'Combined.xyz'
    tf = open(fName, 'w')
    tf.write(f'{len(l1) + len(l2)}\n')
    tf.write('Built with Packmol\n')   
    tf.writelines(l1)
    tf.writelines(l2)
    #print('done writing ', fName)
    
    
f1 = 'N80_Nephrin.xyz'
f2 = 'IC_nck_nw_arp.xyz'
mergeFiles(f1, f2)

print(f'Merged {f1} and {f2} into Combined.xyz')