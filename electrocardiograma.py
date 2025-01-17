# -*- coding: utf-8 -*-
"""electrocardiograma.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11wBzdO_mNGKEgO0J0ESbfSi7ZbOvwVSl
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import convolve as sig_convolve

ecgr=pd.read_csv("ecgr.txt")
ecgr=ecgr['values'].values
fig=plt.figure(figsize=(10,4))
plt.plot(ecgr[0:1000])
plt.show()
print(np.mean(ecgr)) # promedio de la señal

Fs=200
T=1/Fs
N=len(ecgr)
xf=fftfreq(N,T)
xf=np.fft.fftshift(xf)

ecgr_fourier=np.fft.fft(ecgr[:])
print(ecgr_fourier)
ecgr_shift=np.fft.fftshift(ecgr_fourier)
fig=plt.figure(figsize=(15,4))
plt.plot(xf, np.abs(ecgr_shift))
print(np.abs(ecgr_fourier[0])/N)

coef=pd.read_csv("coeficientes.csv")
coef=coef['coef'].values
plt.plot(coef) #sen cardinal 1/Tao (si lo ponemos en el tiempo se llama dualidad de fourier)

Fs=200 #archivo a 200 hrtz por segundo
T=1/Fs #periodo

N=len(coef)#longitud
xf2=fftfreq(N,T) #vector de las frecuencias
xf2=np.fft.fftshift(xf2)

coef_fourier=np.fft.fft(coef[:])                     #transfromada de fourier de la señal previa
coef_shift=np.fft.fftshift(coef_fourier)
fig=plt.figure(figsize=(15,4))
plt.plot(xf2,400*np.abs(coef_shift))
plt.plot(xf,np.abs(ecgr_shift))

ecgr=pd.read_csv("ecgr.txt")
ecgr

conv_result=sig_convolve(ecgr, coef , mode='valid')
plt.plot(conv_result[0:600])

Fs=200
T=1/Fs
N=len(conv_result)

xf=fftfreq(N,T)
xf=np.fft.fftshift(xf)

conv_result_fourier=np.fft.fft(conv_result[:])
print(conv_result_fourier)
conv_result_shift=np.fft.ifftshift(conv_result_fourier)
fig=plt.figure(figsize=(15,4))
plt.plot(xf,np.abs(conv_result_shift))
print(np.abs(conv_result_fourier[0]/N))