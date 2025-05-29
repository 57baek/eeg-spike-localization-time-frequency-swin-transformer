import numpy as np
import pywt

from ..config.parameters import fmin, fmax, num_freq, wv, tf_ds_factor

def morlet_wavelet_transform(segment_ds, fs_ds, mat_path):
    
    try:
        freqs = np.linspace(fmin, fmax, num_freq)
        scales = pywt.frequency2scale(wv, freqs) * fs_ds
        sampling_period = 1 / fs_ds
        coeffs, computed_freqs = pywt.cwt(segment_ds, scales, wv, sampling_period)
        power_spectrogram = np.abs(coeffs) ** 2
        
        # 1/f compensation (mitigating pink noise) 
        trends = 1 / (computed_freqs ** 1.0)
        trends /= np.mean(trends)
        power_spectrogram /= trends[:, np.newaxis]
        
        # log power
        power_spectrogram = np.log(power_spectrogram + 1e-20)
        
        # Downsampling in time
        power_spectrogram = power_spectrogram[:, ::tf_ds_factor]
        tf_fs = fs_ds // tf_ds_factor

        # Normalization
        min_val, max_val = power_spectrogram.min(), power_spectrogram.max()
        power_spectrogram = (power_spectrogram - min_val) / (max_val - min_val)
        if np.isnan(power_spectrogram).any() or np.isinf(power_spectrogram).any():
            print(f"[SKIP] TF MAP WITH NaN OR INF IN {mat_path}")
        
        return power_spectrogram, tf_fs
        
    except Exception as e:
        print(f"[ERROR] TF TRANSFORM FAILED FROM {mat_path}: {e}")
        return None, None