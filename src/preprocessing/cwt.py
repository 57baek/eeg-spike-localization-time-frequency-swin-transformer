import numpy as np
import pywt

from src.configs import parameters


def compute_cwt(eeg_window):
    wavelet_freq = np.linspace(1, 150, 100)
    scales = parameters.sampling_rate_in_Hz / (2 * wavelet_freq)
    cwt_results = []

    for channel in eeg_window:
        cwt_matrix, _ = pywt.cwt(channel, scales, "cmor1.5-1.0")
        power = np.abs(cwt_matrix) ** 2
        cwt_results.append(power)

    return np.array(cwt_results)
