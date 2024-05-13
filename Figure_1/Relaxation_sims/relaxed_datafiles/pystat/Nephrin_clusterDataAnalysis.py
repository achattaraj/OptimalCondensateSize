# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:20:00 2024

@author: Ani Chattaraj
"""

import re, sys, os  
import numpy as np 
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
from numpy import *  
from time import time 
import networkx as nx 
from collections import defaultdict

font = {'family' : 'Arial',
        'size'   : 16}

plt.rc('font', **font)

def ProgressBar(jobName, progress, length=40):
    completionIndex = round(progress*length)
    msg = "\r{} : [{}] {}%".format(jobName, "*"*completionIndex + "-"*(length-completionIndex), round(progress*100))
    if progress >= 1: msg += "\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)
        
    
def calc_RadGy(posList):
    # posList = N,3 array for N sites
    com = np.mean(posList, axis=0) # center of mass
    Rg2 = np.mean(np.sum((posList - com)**2, axis=1))
    return com, np.sqrt(Rg2) 

def readFile(file):
    with open(file,'r') as tf:
        lines = tf.readlines()
    return lines 


def getBlock(lines, str1='', str2='', skipName=True):
    # skipName => whether to return heading  
    i1, i2 = 0, 0
    for i, line in enumerate(lines):
        if re.search(str1, line):
            i1 = i 
        if re.search(str2, line):
            i2 = i 
    if str2 == '':
        i2 = len(lines)
        
    if skipName:
        return lines[i1+1:i2]
    else:
        return lines[i1:i2]


def processCoorBlock(cBlock):
    tmp_frame = array([line.strip().split() for line in cBlock[1:-1]])
    atomId = tmp_frame[:,0].astype(np.int32)
    atomTyp = tmp_frame[:,2].astype(np.int32)
    charge = tmp_frame[:,3].astype(np.float32)
    mId = tmp_frame[:,1].astype(np.int32)
    pos = tmp_frame[:,[4,5,6]].astype(np.float32)
    return atomId, mId, atomTyp, charge, pos

def processBondBlock(bBlock):
    tmp_frame = array([line.strip().split() for line in bBlock[1:-1]])
    bId = tmp_frame[:,0].astype(np.int32)
    bTyp = tmp_frame[:,1].astype(np.int32)
    bPair = tmp_frame[:,[-2,-1]].astype(np.int32)
    return bId, bTyp, bPair 

def calculate_dimensions(pos):
    # Assuming pos is an array of shape (n, 3), where n is the number of points,
    # and each row represents the (x, y, z) coordinates of a point.
    
    # Calculate the range along each axis
    min_vals = np.min(pos, axis=0)
    max_vals = np.max(pos, axis=0)
    
    # The length along each axis is max - min
    lengths = max_vals - min_vals
    
    return lengths

def parseDataFile(dfile):
    lines = readFile(dfile)
    coor_block = getBlock(lines, 'Atoms', 'Velocities')
    bond_block = getBlock(lines, 'Bonds', 'Angles')
    
    aId, mId, atomTyp, charge, pos = processCoorBlock(coor_block)
    _, _, bonds = processBondBlock(bond_block)
   
    a2m = dict(zip(aId, mId))
    mBonds = [(a2m[a1], a2m[a2]) for a1,a2 in bonds if a2m[a1] != a2m[a2]]
    
    bG = nx.Graph() # bead (site/atom) Graph 
    bG.add_edges_from(bonds)
    
    idxList = []
    csList = []
    
    for g in connected_component_subgraphs(bG):
        idx = array([np.where(aId == n) for n in g.nodes()]).flatten()
        idxList.append(idx)
        
        mG = nx.MultiGraph()
        mBonds = [(a2m[b1], a2m[b2]) for b1, b2 in g.edges() if a2m[b1] != a2m[b2] ]
        
        if len(mBonds) == 0:
            csList.append(1)
        else:
            mG.add_edges_from(mBonds)
            csList.append(len(mG.nodes()))
        
    cs_idx = np.argmax(array([len(x) for x in idxList])) # large cluster Id
    
    idx = idxList[cs_idx]
    # returns the largest cluster (atoms, molecules, positions)
    return csList, aId[idx], mId[idx], pos[idx], pos


def getClusterProperty(dfile):
    _, aId, mId, clus_pos, _ = parseDataFile(dfile)
    _, Rg = calc_RadGy(clus_pos)
    a,b,c = calculate_dimensions(clus_pos)
    return Rg, a/2, b/2, c # Lx = a/2, Ly = b/2, Lz = c 

def getMolLocations(dfile, molTyp):
    _, aId, mId, clus_pos, _ = parseDataFile(dfile)
    
    com_clus, Rg_clus = calc_RadGy(clus_pos)
    clus_com_xy_plane = [com_clus[0], com_clus[1], 0]
    
    min_vals = np.min(clus_pos, axis=0)
    max_vals = np.max(clus_pos, axis=0)
    
    radii = (max_vals - min_vals) / 2
    
    dist_stat = {} # distance (x,y,z projection) of molecules from cluster center 
    #radial_dist = {} # radial distance 
    
    for mName, ids in molTyp.items():
        
        tmp_dist = []
        
        for mol in ids:
            idx = np.where(mId == mol)
            com = mean(clus_pos[idx], axis=0)
            distances_from_center = np.abs(com - clus_com_xy_plane)
            norm_dist = distances_from_center/radii 
            tmp_dist.append(norm_dist)
        
        dist_stat[mName] = tmp_dist 
    
    return dist_stat
    
def getClusterDist(csList):
    N, TM = len(csList), sum(csList)
    unique_clusters = sorted(set(csList))
    freq = [csList.count(clus)/N for clus in unique_clusters]
    foTM = [csList.count(clus)*(clus/TM) for clus in unique_clusters]
    return unique_clusters, freq, foTM 
        
def writeData(cs_stat, Rg_sys, Lxyz, mol_dist, sysName='', distSave=False):
    cs, freq, foTM = getClusterDist(cs_stat)
    
    np.savetxt( f'./{sysName}_clusDist.txt', array([cs,freq,foTM]).T,
               fmt='%.4e', header='CS \tFreq \tFoTM')
    
    tmpList = []
    
    
    np.savetxt( f'./{sysName}_Lxyz_Rg.txt', array(Lxyz),
               fmt='%.4e', header='Rg \t\tLx \tLy \tLz')
    
    np.savetxt( f'./{sysName}_Rg_sys.txt', array(Rg_sys),
               fmt='%.4e')
    
    if distSave:
        for mol, dist in mol_dist.items():
            np.savetxt( f'./{mol}_dist_{sysName}.txt', array(dist), 
                       fmt='%.4e', header='d_x d_y d_z')
    return 0 
      

def getStat(dfiles, molType, sysName='', distSave=False):
    mol_dist_stat = defaultdict(list)
    Rg_sys = []
    cs_stat = []
    Lxyz = []
    N_elem = len(dfiles)
    
    print()
    print('System: ', dfiles[0])
    print(f'Processing {N_elem} DATA files ...')
    print()
    
    for i, dfile in enumerate(dfiles):
        ProgressBar('Progress', (i+1)/N_elem)
        csList, _, _, _, pos = parseDataFile(dfile)
        cs_stat.extend(csList)
        
        _, Rg = calc_RadGy(pos)
        Rg_sys.append(Rg)
        
        rg, Lx, Ly, Lz = getClusterProperty(dfile)
        #RgList.append(rg)
        Lxyz.append([rg,Lx,Ly,Lz])
        
        mol_dist = getMolLocations(dfile, molType)
        
        for k, v in mol_dist.items():
            mol_dist_stat[k].extend(v) 
     
    
    writeData(cs_stat, Rg_sys, Lxyz, mol_dist_stat, sysName=sysName, distSave=distSave)

   

   

  