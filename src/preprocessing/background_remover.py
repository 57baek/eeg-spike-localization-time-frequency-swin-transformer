import numpy as np


def subtract_background(cwt_onset, cwt_baseline):
    for i in range(cwt_onset.shape[0]):
        baseline_mean = np.mean(cwt_baseline[i], axis=1).reshape(-1, 1)
        cwt_onset[i] -= baseline_mean
    return cwt_onset
