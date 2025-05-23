from ..config.parameters import pre_sec, post_sec, eeg_ds_factor

def extract_seizure_segments(mat_path, struct_key, pre_sec = pre_sec, post_sec = post_sec, eeg_ds_factor = eeg_ds_factor):
    