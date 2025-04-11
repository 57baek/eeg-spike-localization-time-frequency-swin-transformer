import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from src.configs import parameters


def convert_to_rgb(cwt_results_dB):
    rgb_images = []
    for power in cwt_results_dB:
        rgb = cm.turbo(power)[:, :, :3]
        rgb_images.append(rgb)
    return np.array(rgb_images)


def plot_tf_images(rgb_images, channel_labels, output_dir="results"):
    time_window = parameters.time_window_in_s
    patient_name = parameters.patient_name

    # Create results/patient_name/ directory
    patient_tf_dir = os.path.join(output_dir, patient_name)
    os.makedirs(patient_tf_dir, exist_ok=True)

    for idx, img in enumerate(rgb_images):
        plt.figure(figsize=(8, 6))
        plt.imshow(
            img[::-1],  # Flip vertically
            aspect="auto",
            extent=[-time_window, time_window, 1, 150],
        )
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.title(f"Time-Frequency CWT - Channel {channel_labels[idx]}")
        plt.colorbar(label="Power")
        plt.tight_layout()

        filename = f"channel_{idx:03d}_{channel_labels[idx]}.png"
        filepath = os.path.join(patient_tf_dir, filename)
        plt.savefig(filepath)
        plt.close()

    print(f"Saved {len(rgb_images)} images to '{patient_tf_dir}/'")
