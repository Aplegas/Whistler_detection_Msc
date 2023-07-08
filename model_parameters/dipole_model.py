import numpy as np
#import dipole_codinates as r
from matplotlib import pyplot as plt
#from IPython.core.debugger import set_trace 

#verified values
def electron_density_P(theta,L_value,theta_h,n_h=34600,h=1000e3,O_percent =90,H_percent=8,He_Percent=2,T=1600,R_0=6370e3):
    """electron density model,
    Hydrogen = [0.2,15.2] m = 1
    Hellium  = [1.9,82.3] m = 4
    Oxygen   = [97.9,2.5] m = 16
    mass_e of electron  = 9.10940*10-31 kg 
    Mass of neutron   = 1.67495*10-27 kg 
    Mass of proton    = 1.6726*10-27 kg
    E_i = (0.2,1.9,97.9)
    m_i = (1.67495e-27,1.67495e-27*4.003,1.67495e-27*16.00)
    omega  = 7.2921150e-5
    charge_e =1.60217662e-19"""
    z = z_h_1(theta,L_value,theta_h,h=h,R_0=R_0,g_h=7.33)
    H = Hi(T=1600,g_h=7.33,mi=1.6726e-27 )
    HO = Hi(T=1600,g_h=7.33,mi=1.67495e-27*16.00 )
    He = Hi(T=1600,g_h=7.33,mi=1.67495e-27*4.003 )
    t_1 = (O_percent/100)*np.exp(-z/HO)
    t_2 = (H_percent/100)*np.exp(-z/H)
    t_3 = (He_Percent/100)*np.exp(-z/He)
    #set_trace()
    return n_h*1e6*np.sqrt(t_1+t_2+t_3) 

def DE_1(theta,L_value,theta_h,n_h=34600,h=1000e3):
    """electron density model,
    Hydrogen = [0.2,15.2] m = 1
    Hellium  = [1.9,82.3] m = 4
    Oxygen   = [97.9,2.5] m = 16
    mass_e of electron  = 9.10940*10-31 kg 
    Mass of neutron   = 1.67495*10-27 kg 
    Mass of proton    = 1.6726*10-27 kg
    E_i = (0.2,1.9,97.9)
    m_i = (1.67495e-27,1.67495e-27*4.003,1.67495e-27*16.00)
    omega  = 7.2921150e-5
    charge_e =1.60217662e-19"""
    z = z_h_1(theta,L_value,theta_h,h=h,R_0=6370e3,g_h=7.33)
    t_1 = (0.9)*np.exp(-z/112459.0)
    t_2 = (0.08)*np.exp(-z/1801869.0)
    t_3 = (0.02)*np.exp(-z/449498.0)
    #set_trace()
    return n_h*1e6*np.sqrt(t_1+t_2+t_3) 

def electron_density_A(theta,L_value,n_h=34600,h=500e3,O_percent =97.9,H_percent=0.2,He_Percent=1.9,T=1000,R_0=6370e3):
    """electron density model,
    Hydrogen = [0.2,15.2] m = 1
    Hellium  = [1.9,82.3] m = 4
    Oxygen   = [97.9,2.5] m = 16
    mass_e of electron  = 9.10940*10-31 kg 
    Mass of neutron   = 1.67495*10-27 kg 
    Mass of proton    = 1.6726*10-27 kg
    E_i = (0.2,1.9,97.9)
    m_i = (1.67495e-27,1.67495e-27*4.003,1.67495e-27*16.00)
    omega  = 7.2921150e-5
    charge_e =1.60217662e-19"""
    z = z_h_2(theta,L_value,h=h,R_0=R_0)
    H = 1.1262e3*T
    HO = (1.1262e3*T)/16
    He = (1.1262e3*T)/4
    t_1 = (O_percent/100)*np.exp(-z/HO)
    t_2 = (H_percent/100)*np.exp(-z/H)
    t_3 = (He_Percent/100)*np.exp(-z/He)
    #set_trace()
    return n_h*1e6*np.sqrt(t_1+t_2+t_3) 



def exp_f(theta,theta_h,L_value,n_h=34600,h=500e3,O_percent =97.9,H_percent=0.2,He_Percent=1.9,T=1000,R_0=6370e3):
    H = 1.1262e3*T
    HO = (1.1262e3*T)/16
    He = (1.1262e3*T)/4
    z_h_2(theta,theta_h,h=h,R_0=R_0)
    h_i = [H,HO,He]
    percent = [H_percent,O_percent,He_Percent]
    names = ("$H_{3} \, and \, \eta_{3}$","$H_{1} \, and \, \eta_{1}$","$H_{2} \, and \, \eta_{2}$")
    fig3, ax2 = plt.subplots(constrained_layout=True)
    for i,g,n_i in zip(h_i,names,percent):
        z=-z_h_2(theta,L_value,h=500e3,R_0=6370e3)/i
        #plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))  
        ####
        description = r'$\eta_{i} e^{\left(\frac{R_{b}^{2}-R_{b}R_{0}L \cos ^{2}\theta}{H_{i}R_{0}L \cos ^{2} \theta}\right)}$'
        fig3.suptitle(r'The variation of the {} with latitude, given in Equation 2'.format(description))   
        ax2.set_xlabel(r'Latitude (degrees)')
        ax2.set_ylabel(description)
        ax2.yaxis.set_label_position("right")
        ax2.yaxis.tick_right()
        ax2.plot(theta*(180/np.pi),n_i*np.exp(z),label=r'{}'.format(g))
        plt.legend(loc=2) 
#        plt.grid() 
        plt.show()

def Hi(T=1000,g_h=7.33,mi=1.6726e-27 ):
    k = 1.3807e-23
    return (k*T)/(g_h*mi)

def z_h_1(theta,L_value,theta_h,h=500e3,R_0=6370e3,g_h=7.33):
    R_h= h+R_0
    omega=7.2921159e-5
    R= R_0*L_value*np.cos(theta)**2
    z = R_h-(R_h**2/R)-(omega**2/(2*g_h))*(R**2*np.cos(theta)**2-R_h**2*np.cos(theta_h)**2)
    return z
     

def z_h_2(theta,L_value,h=500e3,R_0=6370e3):
     R_h = R_0+h
     z = R_h-(R_h**2/(R_0*L_value*np.cos(theta)**2))
     return z
    


if __name__== '__main__':
    print()
    
 
