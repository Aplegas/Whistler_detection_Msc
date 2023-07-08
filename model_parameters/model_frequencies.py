import numpy as np

'''Helliwel f_b_eq = 886e3 Hz
   Park     f_b_eq =  873.6e3 Hz
   calcutelated
   f_b_eq = (30e-6*1.76e11)/2*np.pi=841.3e3 Hz'''
   
#Park calculation: ((31.2e-6)*(1.6027663e-19))/(2*np.pi*(9.1093837e-31))
# 873687.1181639388.


def k_0(w,c):
    """forward propagation factor K_0"""
    return w/c

def w_b_H(theta,L_value):
    """Gyrofrequency frequency adpted(Helliwel)"""
    return 2*np.pi*886e3*(1/(L_value**3*np.cos(theta)**6))*np.sqrt(1+3*np.sin(theta)**2) 

def w_p(electron_density):
    """calculating plasma frequency square, model used are,
    ParK model = electron_density_P(theta,L_value,theta_h,n_h=34600,h=1000e3,O_percent =90,H_percent=8,He_Percent=2,T=1600,R_0=6370e3)
    Park model = DE_1(theta,L_value,theta_h,n_h=34600,h=1000e3)
    A model    = electron_density_A(theta,L_value,n_h=34600,h=500e3,O_percent =97.9,H_percent=0.2,He_Percent=1.9,T=1000,R_0=6370e3)
    """
    return 56.4*np.sqrt(electron_density)

def w_p_cm(electron_density):

    """calculating plasma frequency square, model used are,
    intro to plasma Donald A.Gurnett
    ParK model = electron_density_P(theta,L_value,theta_h,n_h=34600,h=1000e3,O_percent =90,H_percent=8,He_Percent=2,T=1600,R_0=6370e3)
    Park model = DE_1(theta,L_value,theta_h,n_h=34600,h=1000e3)
    A model    = electron_density_A(theta,L_value,n_h=34600,h=500e3,O_percent =97.9,H_percent=0.2,He_Percent=1.9,T=1000,R_0=6370e3)
    """
    return 2*np.pi*8980*np.sqrt(electron_density)



def w_b_P(theta,L_value):
    """gyrofrequency frequency adpted(Park)"""
    R_0 = 6370e3
    R = R_0*L_value*np.cos(theta)**2
    return 2*np.pi*8.736e5*(R_0/R)**3*np.sqrt(1+3*np.sin(theta)**2) #8.736e5

def w_b_C(theta,L_value):
    """calculatied(C) gyrofrequency frequency """
    R_0 = 6370e3
    R = R_0*L_value*np.cos(theta)**2
    return (1.6022e-19/(9.1095e-31))*3e-9*(R_0/R)**3*np.sqrt(1+3*np.sin(theta)**2)


def B_Gauss(theta,theta_h):
    """calculating gyrofrequency frequency square"""
    R_0 = 6370e3
    R = (R_0*np.cos(theta)**2)/np.cos(theta_h)**2
    return 0.312*(R_0/R)**3*(1+3*np.sin(theta)**2)**0.5

def B_SI(theta,L_value):
    """calculating gyrofrequency frequency square"""
    R_0 = 6370e3
    R = R_0*L_value*np.cos(theta)**2
    return 30e-6*(R_0/R)**3*(4-3*np.cos(theta)**2)**0.5  #

def w_p_walk(L_value,theta,w_p_eq):
    """Plasma frequency model prof_walker""" 
    return w_p_eq*np.exp(-2.5/(L_value*np.cos(theta)**2))     

def w_b_walk(L_value,theta,w_b_eq):
     """Plasma frequency model prof walker"""
     return (w_b_eq*np.sqrt((4-3*np.cos(theta)**2)))/(L_value**3*np.cos(theta)**6)

if __name__== '__main__':
     print()
