#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 09:11:49 2023

@author: gt2023
"""
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000
from  matplotlib import pyplot as plt
import numpy as np
from generate_synthetic import parallel as mp
import gc
import os
import multiprocessing as mpg
import sys

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=100, cols=100))

plt.rcParams['font.sans-serif'] = "Arial"
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams.update({'font.size': 9})
plt.rcParams["figure.figsize"] = (8,4)
#import tracemalloc

#tracemalloc.start()
electron_densities = np.arange(2050)+50
modeltype = "sferic"
sferic_numb = 3
numb_processors = mpg.cpu_count()-1
numbrGeneratdWhistlers = 60
for n_h in electron_densities:
    #Generally sferic model used do not depend on electron density
    #electron density is used to generate sensable time delays.
    if modeltype=="sferic":
        numbrGeneratdWhistlers = 12
        #Similarly sferic do depend on L-values, L_value dependence is for convienance
        L_valuesets = np.linspace(1.5,2.5,numbrGeneratdWhistlers)
    else:
        L_valuesets = np.linspace(1.5,6,numbrGeneratdWhistlers)
    ChunksL_value = np.array_split(L_valuesets,numb_processors)
    for count,L_values in enumerate(ChunksL_value):
            
        
        start_requred_snr,end_requred_snr,points_requred_snr = 60,count,4
        req_snr_dbs = np.linspace(start_requred_snr,end_requred_snr,points_requred_snr)
        start_bar,end_bar,spacing= 0,2*numb_processors,2
        progresbars = np.array(np.arange(start_bar,end_bar,spacing)+2)
        
        
        mp.generateWhistlers(L_values,n_h,req_snr_dbs,progresbars,numb_processors,modeltype=modeltype,sferic_numb=6)
        os.system('cls' if os.name == 'nt' else 'clear')
        gc.collect()
    
# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('lineno')
# print("[ Top 10 ]")
# for stat in top_stats[:-1]:
#     print(stat)

    



