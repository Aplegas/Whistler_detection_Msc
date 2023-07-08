#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:13:53 2022

@author: workstation
"""
from multiprocessing import Pool
import generate_synthetic.model_evalution as wm

def generateWhistlers(L_values,n_h,req_snr_dbs,progresbars,number_processor,modeltype="whistler",sferic_numb=6):
    
    '''Create whistlers in parallel:
        L_value: flaot
        t: sampling rate array
        n_h: float initial electron density
        progresbars: array 10 bars locations
        e.g [2,4,6,8,10,12,14,16,18,20] spaced by two lines'''
    
    with Pool(number_processor) as p:
        tasks = []
        L_values = L_values
        req_snr_dbs = req_snr_dbs
        progresbars = progresbars
        
        for L_value,barlocation,req_snr_db in zip(L_values,progresbars,req_snr_dbs):
            task = p.apply_async(func=wm.creatWhistler,args=(L_value,n_h,req_snr_db,barlocation,modeltype,sferic_numb))
            tasks.append(task)
         
        for count,task in enumerate(tasks):
            task.wait()
            task.get()
            count = count

