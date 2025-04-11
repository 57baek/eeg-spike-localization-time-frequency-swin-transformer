import numpy as np

from src.configs import parameters
from src.utils.windowing import extract_window
from src.data_loader.patient_loader import load_patient_data
from src.preprocessing.cwt import compute_cwt
from src.preprocessing.background_remover import subtract_background
from src.visualization.plot_tf import convert_to_rgb, plot_tf_images


def main():
    eeg, t0_index, t_neg_index, channel_labels = load_patient_data()

    eeg_window_0 = extract_window(
        eeg, t0_index, parameters.time_window_in_s, parameters.sampling_rate_in_Hz
    )
    eeg_window_neg = extract_window(
        eeg, t_neg_index, parameters.time_window_in_s, parameters.sampling_rate_in_Hz
    )

    cwt_0 = compute_cwt(eeg_window_0)
    cwt_neg = compute_cwt(eeg_window_neg)

    cwt_0_dB = 10 * np.log10(cwt_0 + parameters.epsilon)
    cwt_neg_dB = 10 * np.log10(cwt_neg + parameters.epsilon)

    cwt_0_subtracted = subtract_background(cwt_0_dB, cwt_neg_dB)

    rgb_images = convert_to_rgb(cwt_0_subtracted)

    plot_tf_images(rgb_images, channel_labels, output_dir="results")


if __name__ == "__main__":
    main()
