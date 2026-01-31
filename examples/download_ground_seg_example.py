'''
Example script for downloading segmentation data from TartanGround.

Uses TartanGround (HuggingFace: theairlabcmu/TartanGround) which has 63 environments.

Modalities downloaded:
    seg        — 640x640 Grayscale 8-bit PNG (pixel value = mesh ID from seg_label_map)
    seg_labels — per-env seg_label.json and seg_label_map.json

Disk layout after download:
    {root}/{Env}/
        seg_label.json          (sequential label ID -> name)
        seg_label_map.json      (name -> pixel value in seg PNG)
        Data_{version}/P{NNNN}/
            seg_lcam_front/000000_lcam_front_seg.png
'''

import tartanair as ta

# Set the root folder for the dataset.
ta.init(tartanair_root='DATA_ROOT')

# Download all seg data from TartanGround
ta.download_ground(env = [],
                   version = ['anymal', 'diff', 'omni'],
                   traj = [],
                   modality = ['seg', 'seg_labels'],
                   camera_name = ['lcam_front'],
                   unzip = True,
                   delete_zip = True,
                   num_workers = 8,
                   data_source = 'huggingface')
