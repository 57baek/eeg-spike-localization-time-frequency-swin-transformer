import numpy as np
import pywt

from ..configs import parameters


def extract_eeg_window(eeg, t0_index):
    sampling_window = parameters.sampling_rate_in_Hz * parameters.timeWindow_tf_in_s

    start_index = t0_index - sampling_window
    end_index = t0_index + sampling_window

    return eeg[:, start_index:end_index]


def compute_cwt(eeg_window):
    wavelet_freq = parameters.wavelet_freq
    scales = parameters.sampling_rate_in_Hz / (2 * wavelet_freq)
    cwt_results_raw = []

    for channel in eeg_window:
        cwt_matrix, _ = pywt.cwt(channel, scales, parameters.bandWidth_and_centerFrequency)
        power = np.abs(cwt_matrix) ** 2
        cwt_results_raw.append(power)

    return np.array(cwt_results_raw)


def convert_to_db(cwt_results_raw):
    epsilon = parameters.epsilon

    return 10 * np.log10(cwt_results_raw + epsilon)


def generate_tf_images(eeg, t0_index):
    eeg_window = extract_eeg_window(eeg, t0_index)
    cwt_results_raw = compute_cwt(eeg_window)

    return convert_to_db(cwt_results_raw)
