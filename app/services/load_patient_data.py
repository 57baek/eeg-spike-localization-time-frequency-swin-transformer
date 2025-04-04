import os
import numpy as np
import scipy.io as sio
import re

from ..configs import parameters


def get_channel_labels(channel_mat_path):
    channel_data = sio.loadmat(channel_mat_path)

    return [ch[0] for ch in channel_data["Channel"]["Name"][0]]


def get_eeg_and_metadata(montage_mat_path):
    data = sio.loadmat(montage_mat_path)

    eeg = data["F"]
    time_array = data["Time"].flatten()

    event_labels = [event[0] for event in data["Events"]["label"][0]]

    onset_times = [
        data["Events"]["times"][0][index]
        for index, label in enumerate(event_labels)
        if re.search(parameters.onset_description_pattern, label.lower())
    ]

    return eeg, time_array, onset_times


def find_time_indices(time_array, onset_times):
    if not onset_times:
        raise ValueError("onset_times is empty or None")

    t0 = onset_times[0].item()
    t0_index = np.argmin(np.abs(time_array - t0))
    t_bg_index = np.argmin(np.abs(time_array - (t0 - parameters.bg_time_in_s)))

    return t0_index, t_bg_index


def load_patient_data():
    patient_path = parameters.input_folder
    for subdir in os.listdir(patient_path):
        if (
            subdir.startswith(parameters.subdir_prefix)
            and parameters.subdir_end in subdir
        ):
            subdir_path = os.path.join(patient_path, subdir)

            channel_labels = get_channel_labels(
                os.path.join(subdir_path, parameters.channel_mat_file_name_format)
            )

            eeg, time_array, onset_times = get_eeg_and_metadata(
                os.path.join(subdir_path, parameters.montage_mat_file_name_format)
            )

            t0_index, t_bg_index = find_time_indices(time_array, onset_times)

            return eeg, time_array, t0_index, t_bg_index, channel_labels

    raise ValueError("No valid seizure directory found.")
