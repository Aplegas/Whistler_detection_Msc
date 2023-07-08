#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pathlib
import numpy as np
import time
import pickle
"""
Created on Wed Sep 22 14:36:19 2021

@author: neural
"""

cwd = os.path.dirname(os.path.realpath(__file__))

def saveValues(name,value,dirName='inte_parameters'):
    '''Check if the file is accessable, yes save it else rercurse'''
    direcPath = os.path.join(cwd,'{}'.format(dirName))
    pathlib.Path(direcPath).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(direcPath,'{}.npy'.format(name)),'wb') as f:
            np.save(f,value)

def savedic(name,value,dirName='inte_parameters'):
    '''Check if the file is accessable, yes save it else rercurse'''
    direcPath = os.path.join(cwd,'{}'.format(dirName))
    pathlib.Path(direcPath).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(direcPath,'{}.pkl'.format(name)),'wb') as f:
            pickle.dump(value,f)   
    
        
def loadValues(name,dirName='inte_parameters'):
    '''Check if the file is accessable, yes open it else rercurse'''
    
    direcPath = os.path.join(cwd,'{}'.format(dirName))
    pathlib.Path(direcPath).mkdir(parents=True, exist_ok=True)
    if not(os.access(os.path.join(direcPath,'{}.npy'.format(name)), os.R_OK)):
        time.sleep(2)
        loadValues(name,dirName='inte_parameters')
    else:
         with open(os.path.join(direcPath,'{}.npy'.format(name)),'rb') as f:
             return np.load(f)
         
def loadic(name,dirName='inte_parameters'):
    '''Check if the file is accessable, yes open it else rercurse'''
    direcPath = os.path.join(cwd,'{}'.format(dirName))
    pathlib.Path(direcPath).mkdir(parents=True, exist_ok=True)
    if not(os.access(os.path.join(direcPath,'{}.pkl'.format(name)), os.R_OK)):
        time.sleep(5)
        loadic(name)
    else:
         with open(os.path.join(direcPath,'{}.pkl'.format(name)),'rb') as f:
             return pickle.load(f)          
         
def loadValuesND(name,dirName='inte_parameters'):
    '''Check if the file is accessable, yes open  else rercurse'''
    direcPath = os.path.join(cwd,'{}'.format(dirName))
    pathlib.Path(direcPath).mkdir(parents=True, exist_ok=True)
    if not(os.access(os.path.join( direcPath,'{}.npy'.format(name)), os.R_OK)):
        loadValuesND(name)
    else:
         with open(os.path.join( direcPath,'{}.npy'.format(name)),'rb') as f:
             return np.load(f)         
         
         

     
def makefolder(foldername):
    cwd = os.path.dirname(os.path.realpath(__file__))
    whist_param = os.path.join(cwd,'{}'.format(foldername))
    pathlib.Path(whist_param).mkdir(parents=True, exist_ok=True)
    
if __name__== '__main__':
    print()    

