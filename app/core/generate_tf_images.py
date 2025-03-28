import numpy as np
import pywt

def extract_eeg_window(eeg, index, time_window, sampling_rate):
    sampling_window = sampling_rate * time_window
    start_index = index - sampling_window
    end_index = index + sampling_window
    return eeg[:, start_index:end_index]

def compute_cwt(eeg_window, sampling_rate):
    wavelet_freq = np.linspace(1, 150, 100)
    scales = sampling_rate / (2 * wavelet_freq)
    cwt_results_raw = []
    for channel in eeg_window:
        cwt_matrix, _ = pywt.cwt(channel, scales, 'cmor1.5-1.0')
        power = np.abs(cwt_matrix) ** 2
        cwt_results_raw.append(power)
    return np.array(cwt_results_raw)

def convert_to_db(cwt_results_raw):
    epsilon = 1e-12
    return 10 * np.log10(cwt_results_raw + epsilon)

def generate_tf_images(eeg, index, time_window=20, sampling_rate=1000):
    eeg_window = extract_eeg_window(eeg, index, time_window, sampling_rate)
    cwt_results_raw = compute_cwt(eeg_window, sampling_rate)
    return convert_to_db(cwt_results_raw)