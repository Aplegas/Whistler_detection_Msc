#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:31:48 2021

@author: neural
"""
import numpy as np

def pw(signal):
    '''calculate root mean squared of the signal'''
    return np.mean(signal**2)

def SNR(signal,nsignal):
    '''calculate  the signal to noise ratio SNR in db
     nsignal= noise signal,signal = main signal(measured)
     returns signal to noise ratio in db'''
    return 10*np.log10(pw(signal)**2/pw(nsignal)**2) 
 
def reqN_level(req_snr,signal):
    ''' calulate the required RMS value for noise.
    Required SNR: req_snr in db
    Measured signal: signal
    returns required RMS value
    '''
    return np.sqrt(pw(signal)**2/(10**(req_snr/20)))

def constant_beta(req_snr,signal,nsignal):
    '''calculate the contantconstant_beta that is needed to keep 
    the noise level in a requred RMS level
    nsignal= noise signal,snr= signal to noise ratio(db)
    signal = main signal(measured)
    returns a noise multipler beta (attenuator) '''
    return reqN_level(req_snr,signal)/pw(nsignal)

def req_level_noise(req_snr,signal,nsignal):
    '''
    req_sn : is required SNR in db
    signal: measured signal
    nsignal: Noise signal
    Required noise level
    return: attenuated noise signal'''
    return nsignal*constant_beta(req_snr,signal,nsignal)
    
def whiteNoise(req_snr_db,signal): 
    '''Return white_noise based on required 
    signal noise ratio'''
    signal_power_wm = signal**2
    mean_noise = 0.5
    signal_aveg_power_wm= np.mean(signal_power_wm)  
    signal_aveg_power_db =10*np.log10(signal_aveg_power_wm)
    noise_avg_db = signal_aveg_power_db - req_snr_db
    req_noise__aveg_power = 10**(noise_avg_db/ 10)
    req_noise_signal_vm = np.random.normal(mean_noise, np.sqrt(req_noise__aveg_power), len(signal_power_wm))
    return req_noise_signal_vm

def rayleighdistriN(req_snr_db,signal): 
    '''Generate random rayleigh distribution ''' 
    rayleigh_n = np.random.rayleigh(2*np.std(signal)**2, len(signal))
    noise_level = req_level_noise(req_snr_db,signal,rayleigh_n)
    return noise_level

def raylegh(r):
        stdsim = np.std(r)*((4-np.pi)/2)**0.5
        return (r/stdsim**2)*np.exp(-(r**2/(2*stdsim**2)))

def rayleighFromGuassian(req_snr_db,signal):
    signal=signal
    rayleGass = raylegh(np.abs(signal))
    noise_level = req_level_noise(req_snr_db,signal,rayleGass)
    return noise_level
    
    
