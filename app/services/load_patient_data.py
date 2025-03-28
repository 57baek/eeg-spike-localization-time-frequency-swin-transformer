import os
import numpy as np
import scipy.io as sio

from ..configs import parameters


def get_channel_labels(channel_mat_path):
    channel_data = sio.loadmat(channel_mat_path)
    return [ch[0] for ch in channel_data["Channel"]["Name"][0]]


def get_eeg_and_metadata(montage_mat_path):
    data = sio.loadmat(montage_mat_path)
    eeg = data["F"]
    time_array = data["Time"].flatten()
    event_labels = [event[0] for event in data["Events"]["label"][0]]
    eeg_onset_times = [
        data["Events"]["times"][0][i]
        for i, lbl in enumerate(event_labels)
        if parameters.onset_description in lbl.lower()
    ]
    return eeg, time_array, eeg_onset_times


def find_time_indices(time_array, onset_times):
    t0 = onset_times[0] if onset_times else None
    t0_index = np.argmin(np.abs(time_array - t0)) if t0 else None
    t_neg_60_index = np.argmin(np.abs(time_array - (t0 - 60))) if t0 else None
    return t0_index, t_neg_60_index


# Entry point for loading patient data
def load_patient_data(input_folder, pname):
    patient_path = os.path.join(input_folder, pname)
    for subdir in os.listdir(patient_path):
        if (
            subdir.startswith(parameters.subdir_prefix)
            and parameters.subdir_end in subdir
        ):
            subdir_path = os.path.join(patient_path, subdir)

            channel_labels = get_channel_labels(
                os.path.join(subdir_path, parameters.channel_mat_file_name)
            )
            eeg, time_array, onset_times = get_eeg_and_metadata(
                os.path.join(subdir_path, parameters.montage_mat_file_name)
            )
            t0_index, t_neg_60_index = find_time_indices(time_array, onset_times)

            return eeg, time_array, t0_index, t_neg_60_index, channel_labels

    raise ValueError("No valid seizure directory found.")


def temp_load_patient_data():
    channel_labels = get_channel_labels("data/channel.mat")
    eeg, time_array, onset_times = get_eeg_and_metadata(
        "data/data_block001_montage.mat"
    )
    t0_index, t_neg_60_index = find_time_indices(time_array, onset_times)

    return eeg, time_array, t0_index, t_neg_60_index, channel_labels
