import os
from dotenv import load_dotenv

load_dotenv()

patient_name = os.getenv("PATIENT_NAME")
input_folder = os.path.join("data", patient_name)

channel_mat_file_name = "channel.mat"
montage_mat_file_name = "data_block001_montage.mat"
onset_description_pattern = r"e+e+g+\s*[_]*\s*o+n+s+e+t+"

subdir_prefix = "SZ"
subdir_end = "bipolar_2"

epsilon = 1e-12

sampling_rate_in_Hz = 1000
time_window_in_s = 20
