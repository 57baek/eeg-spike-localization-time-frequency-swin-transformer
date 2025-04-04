import numpy as np

def subtract_background(cwt_db_onset, cwt_db_baseline):
    for i in range(cwt_db_onset.shape[0]):
        mean_db_baseline = np.mean(cwt_db_baseline[i, :, :], axis=1).reshape(-1, 1)
        cwt_db_onset[i, :, :] = cwt_db_onset[i, :, :] - mean_db_baseline
    
    return cwt_db_onset