def extract_window(eeg, index, window_size, rate):
    half_window = rate * window_size
    return eeg[:, index - half_window : index + half_window]
