1. check whether tf_tensor is equal to tf_np if (tf_tensor = torch.tensor(power_spectrogram, dtype=float32)) and (tf_np = tf_tensor.numpy())
2. visualize both _tf.pkl and _tf1.pkl to show that optimized pickle.dump code works
3. try gpu and torch for the visualization and tensor vs. numpy check


INPUT_DIR

INPUT_DIR
    - patient1
        - IOZ
            - seizureData1.mat
            - seizureData2.mat
            - ...
        - NIZ
            - data1.mat
            - data2.mat
            - ...
    - patient2
        - IOZ
            - seizureData1.mat
            - seizureData2.mat
            - ...
        - NIZ
            - data1.mat
            - data2.mat
            - ...
    - ...

OUTPUT_DIR

STRUCT_KEY


Need optimization for both eeg_ds_factor and tf_ds_factor since we could just 
eeg_ds_factor = fs // eeg_fs_target
fs_ds = fs // eeg_ds_factor
tf_ds_factor = fs_ds // tf_fs