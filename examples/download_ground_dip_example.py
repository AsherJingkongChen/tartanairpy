'''
Example script for downloading depth, image, and pose data from TartanGround.

Uses TartanGround (HuggingFace: theairlabcmu/TartanGround) which has 63 environments.

Robot versions:
    omni (P0xxx) — omnidirectional robot
    diff (P1xxx) — differential drive robot

Modalities downloaded:
    image — 640x640 RGB 8-bit PNG
    depth — 640x640 RGBA 8-bit PNG (float32 z-depth encoded as 4 x uint8)
    meta  — pose files + metadata per trajectory (required for TartanGround;
            TartanAir V2 bundles pose inside image/depth zips instead)

Disk layout after download:
    {root}/{Env}/Data_{version}/P{NNNN}/
        image_lcam_front/000000_lcam_front.png
        depth_lcam_front/000000_lcam_front_depth.png
        pose_lcam_front.txt  (x y z qx qy qz qw per line, NED frame)
        pose_{other_cameras}.txt  (from meta, can be ignored)

Camera intrinsics are fixed across all environments:
    fx = fy = 320, cx = cy = 319.5, image size = 640x640, FOV = 90 degrees.
'''

import tartanair as ta

# Set the root folder for the dataset.
ta.init(tartanair_root='DATA_ROOT')

# Download all depth, image, and meta data from TartanGround
ta.download_ground(env = [],
                   version = ['anymal', 'diff', 'omni'],
                   traj = [],
                   modality = ['depth', 'image', 'meta'],
                   camera_name = ['lcam_front'],
                   unzip = True,
                   delete_zip = True,
                   num_workers = 8,
                   data_source = 'huggingface')
