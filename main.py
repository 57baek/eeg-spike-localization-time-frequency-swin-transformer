from app.services.load_patient_data import load_patient_data
from app.core.generate_tf_images import generate_tf_images

eeg, time_array, t0_index, t_bg_index, channel_labels = load_patient_data()

generate_tf_images(eeg, t0_index)
