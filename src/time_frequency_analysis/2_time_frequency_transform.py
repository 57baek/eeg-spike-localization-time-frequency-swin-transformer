import numpy as np
import pywt

from ..config.parameters import fmin, fmax, num_freq, tf_ds_factor, wv

def morlet_wavelet_transform(segment_ds, fs_ds):
    
    try:
        freqs = np.linspace(fmin, fmax, num_freq)
        tf_ds = fs_ds // tf_ds_factor
        
        