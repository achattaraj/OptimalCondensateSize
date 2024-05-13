# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:35:30 2022

@author:Ani Chattaraj
"""
import numpy as np 


def writeXYZ(molName, seq, typName):
    print(f'Writing XYZ file for {molName} monomer ...')
    with open(f'{molName}_mono.xyz', 'w') as tf:
        tf.write(f'{len(seq)}\n')
        tf.write(f'{molName}\n')
        xcoor = 5 
        for bead in seq:
            tf.write(f'{typName[bead]}      {xcoor}      0     0\n')
            xcoor += 5
    print('... done!')
    print()

def writePolyLT(molName, seq, typName, mass):
    print(f'Writing LT file for {molName} ...')
    idList = np.arange(1, len(seq)+1, 1)
    N_bds = len(seq) # number of beads per molecule
    qList = [0]*N_bds # charge of beads
    with open(f'{molName}.lt', 'w') as tf:
        tf.write(f'{molName}' + ' {\n\n')
        
        tf.write('write_once("Data Masses") { \n')
        for typ,name in typName.items():
            tf.write(f'@atom:{name}  {mass[typ]}\n')
        tf.write('} \n\n')
        
        tf.write('write("Data Atoms") { \n')
        for i, bead in enumerate(seq):
            tf.write(f'$atom:{i+1} $mol:. @atom:{typName[seq[i]]} {qList[i]} 0 0 0\n')
        tf.write('} \n\n')
        
        tf.write('write("Data Bonds") { \n')
        for i in range(N_bds - 1):
            tf.write(f'$bond:b{i+1}    @bond:Bond   $atom:{idList[i]}  $atom:{idList[i+1]}\n') 
        tf.write('} \n\n')
        
        tf.write('write("Data Angles") { \n')
        for i in range(N_bds - 2):
            tf.write(f'$angle:a{i+1}    @angle:Angle   $atom:{idList[i]}  $atom:{idList[i+1]}  $atom:{idList[i+2]}\n')
        tf.write('} \n\n')
        
        tf.write('} \n' + f'#{molName}')
        
    print('... done!')
    print()
    
 
# site idx (1,2,3,...) is defined within each molecule type.
# you can use same idx for diiferent mol-type    
# first molecule    
fName1 = 'Nephrin'
seq1 = [3,2,2,1,2,2,1,2,2,1]
typName1 = {3:'Anchor', 2:'NephL', 1:'pY'}
mass1 = {1:450, 2: 450, 3:1000}

writePolyLT(fName1, seq1, typName1, mass1)
writeXYZ(fName1, seq1, typName1)

# second molecule    
fName2 = 'Nck'
seq2 = [2,1,1,3,1,1,3,1,1,3]
typName2 = {2:'SH2', 3:'SH3', 1:'nckL'}
mass2 = {2: 11000, 3: 7000, 1:450}

writePolyLT(fName2, seq2, typName2, mass2)
writeXYZ(fName2, seq2, typName2)

# third molecule    
fName3 = 'NWASP'
seq3 = [4,1,1,4,1,1,4,1,1,4,1,1,4,1,1,4,1,1,5]
typName3 = {4:'PRM', 1:'nwL', 5:'VCA'}
mass3 = {4:450, 1:450, 5:450}

writePolyLT(fName3, seq3, typName3, mass3)
writeXYZ(fName3, seq3, typName3)

# fourth molecule    
fName4 = 'Arp23'
seq4 = [1,2,1]
typName4 = {1:'Arp', 2:'arpL'}
mass4 = {1:450, 2:20000}

writePolyLT(fName4, seq4, typName4, mass4)
writeXYZ(fName4, seq4, typName4)

        
        
        
        
        
    
    


 