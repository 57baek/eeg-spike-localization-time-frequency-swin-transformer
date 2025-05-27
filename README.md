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