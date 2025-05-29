import scipy.io
import numpy as np
import scipy.signal

from ..config.parameters import pre_sec, post_sec, eeg_ds_factor, min_segment_len_sec


def extract_seizure_segment(mat_path, struct_key):
    if post_sec + pre_sec < min_segment_len_sec:
        raise ValueError(f"SEGMENT TOO SHORT: {post_sec + pre_sec}s")

    try:
        mat = scipy.io.loadmat(mat_path, struct_as_record=False, squeeze_me=True)
        data_struct = mat[struct_key]

        sz = data_struct.SZ
        fs = data_struct.Fs
        T = data_struct.T

        if T is None or len(np.atleast_1d(T)) < 1 or np.isnan(T[0]):
            print(f"[SKIP] INVALID OR MISSING SEIZURE ONSET IN {mat_path}")
            return None, None, None

        onset_idx = int(T[0])
        pre_idx = int(pre_sec * fs)
        post_idx = int(post_sec * fs)

        if sz.ndim == 2:
            sz = sz[0]

        start = max(0, onset_idx - pre_idx)
        end = min(len(sz), onset_idx + post_idx)
        segment = sz[start:end]

        segment_ds = scipy.signal.resample(segment, len(segment) // eeg_ds_factor)
        fs_ds = fs // eeg_ds_factor
        tf_ons = int(pre_sec)

        if start == 0:
            tf_ons = onset_idx // fs

        return segment_ds, fs_ds, tf_ons

    except Exception as e:
        print(f"[ERROR] FAILED TO EXTRACT SEIZURE FROM {mat_path}: {e}")
        return None, None, None
