#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 16:54:13 2021

@author: neural
"""
import numpy as np
import generate_synthetic.simpleInfoLogger as sf
#from IPython.core.debugger import set_trace

def sferic_x_0(I_0,w,t_0,x_0,c,sferic_t):
    "excitation function"
    return (2/w)*np.sin(w*t_0*0.5)*np.exp(-1j*w*(sferic_t*0.5))

def sferic_x_n(I_0,w,t_0,x_0,x_n,c):
    "excitation function before the boundry"
    return (2*I_0/w)*np.sin(w*t_0*0.5)*np.exp(-1j*w*((t_0*0.5)+(x_0+x_n)/c))

def sferic_x_n_invers_fourier(I_0,w,t_0,x_0,x_n,L_value,c,t,contr_t,n_h,barlocation):
    """simple rectangular impulse,excitation is at:
    x_n <= x_0.x_0 is at the boundary closen to be R_0+h.
    x_n,is the distance before the boundary"""
    sf.processbar(contr_t,t,barlocation,L_value,n_h,modeltype="sferic")
    return np.real(sferic_x_n(I_0,w,t_0,x_0,x_n,c)*np.exp(1j*(w*t)))


def sferic_x_0_invers_fourier(I_0,w,t_0,x_0,c,t,contr_t,L_value,n_h,barlocation,*sferic_para):
    """simple rectangular impulse,excitation is at:
    x_n <= x_0.x_0 is at the boundary closen to be R_0+h.
    x_n,is the distance before the boundary"""
    sf.processbar(contr_t,t,barlocation,L_value,n_h,modeltype="sferic")
    numb_sferic = sferic_para[0]
    #set_trace()
    if numb_sferic == 2:
        s_1 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[1])*np.exp(1j*(w*t)))
        s_2 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[2])*np.exp(1j*(w*t)))
        return s_1+s_2
    elif numb_sferic == 3:
        s_1 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[1])*np.exp(1j*(w*t)))
        s_2 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[2])*np.exp(1j*(w*t)))
        s_3 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[3])*np.exp(1j*(w*t)))
        return s_1+s_2+s_3
    elif numb_sferic == 4:
        s_1 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[1])*np.exp(1j*(w*t)))
        s_2 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[2])*np.exp(1j*(w*t)))
        s_3 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[3])*np.exp(1j*(w*t)))
        s_4 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[5])*np.exp(1j*(w*t)))
        return s_1+s_2+s_3+s_4
    elif numb_sferic == 5:
        s_1 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[1])*np.exp(1j*(w*t)))
        s_2 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[2])*np.exp(1j*(w*t)))
        s_3 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[3])*np.exp(1j*(w*t)))
        s_4 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[4])*np.exp(1j*(w*t)))
        s_5 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[5])*np.exp(1j*(w*t)))
        return s_1+s_2+s_3+s_4+s_5
    elif numb_sferic == 6:
        s_1 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[1])*np.exp(1j*(w*t)))
        s_2 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[2])*np.exp(1j*(w*t)))
        s_3 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[3])*np.exp(1j*(w*t)))
        s_4 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[4])*np.exp(1j*(w*t)))
        s_5 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[5])*np.exp(1j*(w*t)))
        s_6 = np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[5])*np.exp(1j*(w*t)))
        return s_1+s_2+s_3+s_4+s_5+s_6
    else: 
        return np.real(sferic_x_0(I_0,w,t_0,x_0,c,sferic_para[1])*np.exp(1j*(w*t)))
    
        
def whis_homo(w,t_0,c,w_p,w_b,t,x,x_0,I_0,L_value,n_h,contr_t,barlocation,sferic_t):
      '''This is  homogeneous whistler without loss 
      .The homogeneous refers to constant gyrofrequency and plasmafrequency.'''
      I_0_x=sferic_x_0(I_0,w,t_0,x_0,c,sferic_t)
      k_0 = w/c
      k_1 = k_0*np.sqrt(1+(w_p**2/(w*(w_b-w))))
      s=np.real(I_0_x*(k_0/(k_0+k_1))*np.exp(1j*(w*t-k_1*(x-x_0))))
      sf.processbar(contr_t,t,barlocation,L_value,n_h,modeltype="whistler")
      return s


def whis_homo_with_los(w,t_0,c,w_p,w_b,t,x,x_0,I_0,L_value,contr_t,n_h,v_c,barlocation):                     
    '''This is  homogeneous whistler with loss 
    .The homogeneous refers to constant gyrofrequency and plasmafrequency.
    This model includes collison in plasma.'''
    
    I_0_x = sferic_x_0(I_0,w,t_0,x_0,c)
    k_0 = w/c  
    denominator=(1+((v_c**2+2*1j*w*v_c)/(w_b**2-w**2)))
    numerator = 1-(((v_c**2*(w_b**2-w**2)+ 1j*v_c*(2*w*(w_p**2-w**2))+w_p**2*w_b))/(w_p**2*w_b*w+w**2*(w_p**2+w_b**2-w**2)))
    k_1 = k_0*np.sqrt(1+(w_p**2/(w*(w_b-w)))) 
    K_1 = k_1*np.sqrt(np.real(numerator/denominator))
    sf.processbar(contr_t,t,barlocation,L_value,n_h,modeltype="whistler")
    return np.real(I_0_x*(k_0/(k_0+K_1))*np.exp(1j*(w*t-K_1*(x-x_0))))

def timeintegral(theta_h,theta,L_value,w,w_b,w_p,c=3e8,R_0 = 6370e3,simps=False):
    '''This an integral of the time function'''
    time = -(1/c)*((w_p*R_0*L_value*np.cos(theta)*(1+3*np.sin(theta)**2)**0.5)/(w**0.5*w_b**0.5*(1-(w/w_b))**1.5))
    return time
