# --------------------
# time_frequency_analysis.1_extract_seizure_segment
# --------------------
pre_sec = 30
post_sec = 50
min_segment_len_sec = 60

eeg_ds_factor = 2

# --------------------
# time_frequency_analysis.2_time_frequency_transform
# --------------------
wv = 'cmor1.5-1.0'
fmin = 1
fmax = 150
num_freq = 150

tf_ds_factor = 50
