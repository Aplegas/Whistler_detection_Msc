import numpy as np
from scipy import integrate
import os 
import pathlib
from model_parameters import  dipole_model as dp
from model_parameters import model_frequencies as mf
import generate_synthetic.plot_spectro as ps
#from IPython.core.debugger import set_trace
import generate_synthetic.saveLoadValues  as sv
from  model_parameters import dipole_codinates as r
import generate_synthetic.signal_to_noise as sn
#import timedelay as td
import generate_synthetic.Random_parameters as rp
import generate_synthetic.whist_sfer_wave_models as wwm
import time

def creatWhistler(L_value,n_h,req_snr_db,barlocation,modeltype="sferic",sferic_numb=6):
    cwd = os.path.dirname(os.path.realpath(__file__))

    dirName1 = 'amplitudeST'
    dirName2 = 'amplitudeST_noise'
    dirName3 = 'spectrogram'
    dirName4 = 'spectrogram_no_axis'
    dirName5 = 'spectrogram_noise'
    dirName6 = 'spectrogram_noise_no_axis'
    dirName7 = 'amplitude_arrays'
    dirName8 = 'amplitude_arrays_noise'

    
    
    if modeltype == "sferic":
        Parendir = direcPath1 = os.path.join(cwd,"Generated_sferics")
    elif modeltype == "whistler":
        Parendir = direcPath1 = os.path.join(cwd,"Generated_whistlers")
    else:
        print("In the main.py file select 'whistler' or 'sferic' for modeltype.")
        time.sleep(5)
        exit()
        
    pathlib.Path(Parendir).mkdir(parents=True, exist_ok=True)
    direcPath1 = os.path.join(Parendir,'{}'.format(dirName1))
    direcPath2 = os.path.join(Parendir,'{}'.format(dirName2))
    direcPath3 = os.path.join(Parendir,'{}'.format(dirName3))
    direcPath4 = os.path.join(Parendir,'{}'.format(dirName4))
    direcPath5 = os.path.join(Parendir,'{}'.format(dirName5))
    direcPath6 = os.path.join(Parendir,'{}'.format(dirName6))
    direcPath7 = os.path.join(Parendir,'{}'.format(dirName7))
    direcPath8 = os.path.join(Parendir,'{}'.format(dirName8))
    
    pathlib.Path(direcPath1).mkdir(parents=True, exist_ok=True)
    pathlib.Path(direcPath2).mkdir(parents=True, exist_ok=True)
    pathlib.Path(direcPath3).mkdir(parents=True, exist_ok=True)
    pathlib.Path(direcPath4).mkdir(parents=True, exist_ok=True)
    pathlib.Path(direcPath5).mkdir(parents=True, exist_ok=True)
    pathlib.Path(direcPath6).mkdir(parents=True, exist_ok=True)
    pathlib.Path(direcPath7).mkdir(parents=True, exist_ok=True)
    pathlib.Path(direcPath8).mkdir(parents=True, exist_ok=True)
    
    L_value = L_value
    x_0 = 1000e3
    h= 1000e3
    theta_h = r.theta_h(h,L_value,R_E=6370e3)
    I_0 = 1 
    f_i = 300
    n_h = n_h
    
    electron_density = dp.DE_1(0,L_value, theta_h,n_h)
    w_b = mf.w_b_P(0,L_value)
    w_p = mf.w_p(electron_density)
    if L_value < 3:
        f_f = 20000 #rp.RandPara(4000,15000,8)
        w_f = 2*np.pi*f_f
    elif L_value > 3:
        w_f =  w_b/2
    elif modeltype == "sferic":
        f_f = 20000
        w_f = 2*np.pi*f_f
        
    w_i = 2*np.pi*f_i
    
    samp_intvls = integrate.quad(wwm.timeintegral,theta_h,0,args=(theta_h,L_value,w_i,w_b,w_p))[0]
    fs = 44100
    T= 1/fs
    N= int(fs*samp_intvls)
    ts = np.arange(N)*T
    
    
    #theta_h = r.theta_h(h,L_value,R_0=6370e3)
    degrees = np.linspace(theta_h,0,N)
    xs = r.arclenlength(degrees,theta_h,r.R_h(h,R_E=6370e3))
    Z_0 = 120*np.pi
    t_0 = 0.25e-3 
    c = 3e8
    I_0 = 1  
    
  
    w = np.array(np.linspace(w_i,w_f,N))
    contr_t = ts
    sferic_t = t_0 # defalut sferic_t by theory
   
   
    fileName = "N{}_t{}_L{}_{}_{}_h_n{}_{}_{}_{}_{}_{}_{}_{}{}".format(N,samp_intvls,"%4f" % L_value,"%4f" % theta_h,h,n_h,w_i/2*np.pi,fs,w_b,w_p,t_0,I_0,req_snr_db,".png")
    fileNamenpy = "N{}_t{}_L{}_{}_{}_h_n{}_{}_{}_{}_{}_{}_{}_{}".format(N,samp_intvls,"%4f" % L_value,"%4f" % theta_h,h,n_h,w_i/2*np.pi,fs,w_b,w_p,t_0,I_0,req_snr_db)
    
    if modeltype == "whistler":
        I_result = [(-Z_0/(4*np.pi))*integrate.simps(wwm.whis_homo(w,t_0,c,w_p,w_b,t,x,x_0,I_0,L_value,n_h,contr_t,barlocation,sferic_t), w) for t,x in zip(ts,xs)]
    else:
        sferic_para = [sferic_numb]
        for _ in range(sferic_numb):
            sferic_delta = rp.RandPara1(ts[0],ts[len(ts)-100])
            sferic_para.append(sferic_delta)
        sferic_para = tuple(sferic_para)
    
       
        I_result = [(-Z_0/(4*np.pi))*integrate.simps(wwm.sferic_x_0_invers_fourier(I_0,w,t_0,x_0,c,t,contr_t,L_value,n_h,barlocation,*sferic_para), w) for t in ts]
    
         
    
    META = {"N":N,"L_value":L_value,"minimum frequency":w_i/(2*np.pi),"gyrofrequency":w_b/(2*np.pi),"plasmafrequency":w_p/(2*np.pi),"samples interval":samp_intvls,"sample rate":fs,"impulse duration (t_0)":t_0,"reference height":h,"sferic amplitude (I_0)":I_0,"SN":req_snr_db}
    time_axis = np.array(ts)
    wave_func = np.array(I_result)
    N_wave_func = wave_func + sn.rayleighdistriN(req_snr_db,wave_func)
    ps.PlotTime(time_axis,wave_func,fig=1,fileID=fileName,dirName = direcPath1)
    ps.PlotTime(time_axis,N_wave_func,fig=2,fileID=fileName,dirName = direcPath2)
    ps.plotSpec_PSD(fs,wave_func,fig=3,fileID=fileName,deco='on',dirName = direcPath3)
    ps.plotSpec_PSD(fs,wave_func,fig=4,fileID=fileName,deco='off',dirName = direcPath4)
    ps.plotSpec_PSD(fs,N_wave_func,fig=5,fileID=fileName,deco='on',dirName = direcPath5)
    ps.plotSpec_PSD(fs,N_wave_func,fig=6,fileID=fileName,deco='off',dirName = direcPath6)
   
   
    ps.SavePropagValuesAsMetadata(fileName, direcPath1,META)
    ps.SavePropagValuesAsMetadata(fileName,direcPath2,META)
    ps.SavePropagValuesAsMetadata(fileName,direcPath3,META)
    
    ps.SavePropagValuesAsMetadata(fileName,direcPath4,META)
    ps.SavePropagValuesAsMetadata(fileName,direcPath5,META)
    ps.SavePropagValuesAsMetadata(fileName,direcPath6,META)
    
    sv.saveValues(fileNamenpy,wave_func,dirName=direcPath7)
    sv.saveValues(fileNamenpy,N_wave_func,dirName=direcPath8)
    #set_trace()
    #plt.show()
            

# barlocation =2
# L_value = 1.7  
# n_h = 1000 
# req_snr_db=3
# creatWhistler(L_value,n_h,req_snr_db,barlocation)
# # creatWhistler(L_value,n_h,req_snr_db,barlocation)
# # creatWhistler(L_value,t,n_h,barlocation)   
