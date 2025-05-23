import scipy.io
import numpy as np
import scipy.signal

from ..config.parameters import pre_sec, post_sec, eeg_ds_factor, min_segment_len_sec


def extract_seizure_segments(mat_path, struct_key):
    if post_sec + pre_sec < min_segment_len_sec:
        raise ValueError(
            f"Segment too short (change pre_sec and post_sec): {post_sec + pre_sec}s"
        )

    try:
        mat = scipy.io.loadmat(mat_path, struct_as_record=False, squeeze_me=True)
        data_struct = mat[struct_key]

        sz = data_struct.SZ
        fs = data_struct.Fs
        T = data_struct.T

        if T is None or len(np.atleast_1d(T)) < 1 or np.isnan(T[0]):
            print(f"[SKIP] Invalid or missing seizure onset in: {mat_path}")
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
        tf_ons = pre_idx // fs

        if start == 0:
            tf_ons = onset_idx // fs

        return segment_ds, fs_ds, tf_ons

    except Exception as e:
        print(f"[ERROR] Failed to extract seizure from {mat_path}: {e}")
        return None, None, None
