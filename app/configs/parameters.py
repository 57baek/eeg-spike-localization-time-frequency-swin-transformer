import os
import numpy as np

patient_name = "some_patient_name"

input_folder = os.path.join("some_patient_data_directory_path", patient_name)

channel_mat_file_name_format = "channel.mat"

montage_mat_file_name_format = "data_block001_montage.mat"

onset_description_pattern = r"eeg[\s_]*onset"

subdir_prefix = "SZ"

subdir_end = "bipolar_2"

bg_time_in_s = 60

timeWindow_tf_in_s = 20

sampling_rate_in_Hz = 1000

wavelet_freq = np.linspace(1, 150, 100)

bandWidth_and_centerFrequency = "cmor1.5-1.0"

epsilon = 1e-12
