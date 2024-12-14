# -*- coding: utf-8 -*-
"""frecuencias.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kj06Xxh7fYhcuY_9GlPH6nC6qfRlqoBn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import convolve as sig_convolve

ecgr=pd.read_csv("ecgr.txt")
ecgr=ecgr['values'].values
fig=plt.figure(figsize=(10,4))
plt.plot(ecgr)
plt.show()
ecgr

Fs=200 #archivo a 200 hrtz por segundo
T=1/Fs #periodo
N=len(ecgr)#longitud
xf=fftfreq(N,T) #vector de las frecuencias
xf=np.fft.fftshift(xf)

ecgr_fourier=np.fft.fft(ecgr[:])
ecgrf_shift=np.fft.fftshift(ecgr_fourier)
#fig.plot.fig(figize=(15,4))
print(ecgr_fourier)
plt.plot(xf,np.abs(ecgrf_shift))
plt.plot(np.abs(ecgr_fourier))

ecgr=pd.read_csv("ecgr.txt")
ecgr