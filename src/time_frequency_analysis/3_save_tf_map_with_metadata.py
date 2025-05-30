import scipy.io
import os
import pickle


def save_tf_map(
    mat_path, input_dir, output_dir, struct_key, tf_ons, tf_fs, power_spectrogram
):
    rel_path = os.path.relpath(mat_path, input_dir)
    rel_dirname = os.path.dirname(rel_path)
    target_dir = os.path.join(output_dir, rel_dirname)
    os.makedirs(target_dir, exist_ok=True)

    base = os.path.basename(mat_path)
    filename = os.path.splitext(base)[0] + "_tf.pkl"
    out_path = os.path.join(target_dir, filename)

    mat = scipy.io.loadmat(mat_path, struct_as_record=False, squeeze_me=True)
    data_struct = mat[struct_key]
    tf_ons_idx = tf_ons * tf_fs

    with open(out_path, "wb") as f:
        pickle.dump(
            {
                "tf_map": power_spectrogram,
                "SZ": getattr(data_struct, "SZ", None),
                "BG": getattr(data_struct, "BG", None),
                "pathology": getattr(data_struct, "pathology", None),
                "outcome": getattr(data_struct, "outcome", None),
                "is_ioz": getattr(data_struct, "is_ioz", None),
                "loc": getattr(data_struct, "loc", None),
                "T": getattr(data_struct, "T", None),
                "chn_name": getattr(data_struct, "chn_name", None),
                "Fs": getattr(data_struct, "Fs", None),
                "sz_name": getattr(data_struct, "sz_name", None),
                "tf_onset": tf_ons_idx,
                "tf_Fs": tf_fs,
            },
            f,
        )
