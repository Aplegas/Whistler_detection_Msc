
from  matplotlib import pyplot as plt
#from scipy import signal
import numpy as np
import pathlib
import os 
import warnings
from PIL import Image
from PIL.PngImagePlugin import PngInfo
#from IPython.core.debugger import set_trace

cwd = os.path.dirname(os.path.realpath(__file__))
dirName1 = 'testfile_array'
dirName2 = 'testfile_spectro'
direcPath1 = os.path.join(cwd,'{}'.format(dirName1))
direcPath2 = os.path.join(cwd,'{}'.format(dirName2))

def SavePropagValuesAsMetadata(fileName,dirpath,metadatadic):
    '''Save propagation values as metadata
    parameters: filename, directory path, metadata dictionary'''
    targetImage = Image.open(os.path.join(dirpath,'{}'.format(fileName)))
    metadata = PngInfo()
    for Key,Value in zip(metadatadic.keys(),metadatadic.values()):
        metadata.add_text('{}'.format(Key),'{}'.format(Value))
    targetImage.save(os.path.join(dirpath,'{}'.format(fileName)), pnginfo=metadata)


def ReadPropagValueFromMetadata(fileName,dirpath):
    '''Read the propagation data from an image'''
    targetImage = Image.open(os.path.join(dirpath,'{}'.format(fileName)))
    return targetImage.text


def plotSpec_M(fs,signalArr,fig=2,fileID='',deco='on',dirName ='whistlers_spectrogram'):
    '''fs= sampling frequency,signal= is the electric field signal
    (integrated signa) and fileID=name of the file,
    dirNane=directory name and fig=figure number
    and img=allow for plotting image instead of graph with ticks'''
    spectrogram = os.path.join(cwd, '{}'.format(dirName))
    pathlib.Path(spectrogram).mkdir(parents=True, exist_ok=True)
    
    
    fig ='fig{}'.format(fig)
    fig, ax = plt.subplots()
    
  
    cmap = plt.get_cmap('jet')
    vmin = 10*np.log10(np.max(signalArr)) - 100  # hide anything below -100 dBc
    #cmap.set_under(color='k', alpha=None)
    
    NFFT = 128
    pxx,  freq, t, cax = ax.specgram(signalArr/(NFFT/2), Fs=fs, mode='psd', NFFT=NFFT, noverlap=NFFT/2, vmin=vmin, cmap=cmap, window=np.hamming(128))
    #PSD = power spectral density 
   
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.tight_layout()
    
    if deco.lower() =='off':
        plt.axis('off')
        plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
        fig.savefig(os.path.join(spectrogram,'{}'.format(fileID)),format = "png",dpi=300)
    elif deco.lower() =='on':
         clb= fig.colorbar(cax)               
         clb.ax.tick_params(labelsize=8) 
         clb.set_label(r'$10\log_{10}\left(V^{2} m^{-1} Hz^{-1}\right) \left[dB\right]$', fontsize=12,rotation=90         )
         plt.title("The plot of Frequency (F) vs Time (t)",y=1.1)
         fig.savefig(os.path.join(spectrogram,'{}'.format(fileID)),format = "png",dpi=fig.dpi)
         warnings.filterwarnings("ignore") #ignoring deprecation warning for zoom()
    plt.close(fig)

def plotSpec_PSD(fs,signalArr,fig=2,fileID='',deco='on',dirName ='whistlers_spectrogram',m=85,NFFT = 256):
    '''fs= sampling frequency,signal= is the electric field signal
    (integrated signa) and fileID=name of the file,
    dirNane=directory name and fig=figure number
    and img=allow for plotting image instead of graph with ticks'''
    spectrogram = os.path.join(cwd, '{}'.format(dirName))
    pathlib.Path(spectrogram).mkdir(parents=True, exist_ok=True)
    
    
    fig ='fig{}'.format(fig)
    fig, ax = plt.subplots()
    
  
    cmap = plt.get_cmap('jet')
    vmin = 20*np.log10(np.max(signalArr)) - m  # hide anything below -100 dBc
    NFFT =  NFFT
    pxx,  freq, t, cax = ax.specgram(signalArr/(NFFT/2), Fs=fs, mode='magnitude', NFFT=NFFT, noverlap=NFFT/2, vmin=vmin, cmap=cmap, window=None)
    #PSD = power spectral density 
   
    
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.tight_layout()
    
    if deco.lower() =='off':
        plt.axis('off')
        plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
        fig.savefig(os.path.join(spectrogram,'{}'.format(fileID)),format = "png",dpi=300)
    elif deco.lower() =='on':
         clb= fig.colorbar(cax)               
         clb.ax.tick_params(labelsize=8) 
         clb.set_label(r'$20\log_{10}\left(|V m^{-1}| Hz^{-1}\right) \left[dB\right]$', fontsize=12,rotation=90)
         plt.title("The plot of Frequency (F) vs Time (t)",y=1.1)
         fig.savefig(os.path.join(spectrogram,'{}'.format(fileID)),format = "png",dpi=300)
         warnings.filterwarnings("ignore") #ignoring deprecation warning for zoom()
    plt.close(fig)
    

def PlotTime(time,signalArr,fig =1,fileID='',dirName ='whistlers_Amplitudes'):
    '''fs= sampling frequency,signal= is the electric field signal
    (integrated signa) and fileID=name of the file,
    dirNane=directory name, fig=figure number
    '''
    
    Amplitude = os.path.join(cwd,'{}'.format(dirName))
    pathlib.Path(Amplitude).mkdir(parents=True, exist_ok=True)
    
    fig ='fig{}'.format(fig)
    fig, ax = plt.subplots()
    ax.set_title("The plot of time (t) vs Electric field (E)",y=1.1) 
    ax.plot(time,signalArr)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Electric field [V/m]")
    
    fig.savefig(os.path.join(Amplitude,'{}'.format(fileID)),format = "png",dpi=fig.dpi)
    plt.close(fig)
    

if __name__== '__main__':
    print()
    
    