from get_ref import *
import os
from scipy.io import loadmat
import numpy as np

def load_multicam(dataset, group_name, section_number, optional_frames=None):
    home_path = get_ref(dataset)

    depth = 'depthRender'
    classes = 'groundtruth'
    file_format = 'mayaProject.{idx:06d}.png'
    base_path = os.path.join(home_path, group_name, str(section_number))

    depth_path = os.path.join(base_path, 'images', depth, '{camera_name}', file_format)
    # print(depth_path.format(camera_name='Cam1', idx=25))
    class_path = os.path.join(base_path, 'images', classes, '{camera_name}', file_format)

    print('Loading groundtruth file {:d} ...'.format(section_number))
    groundtruth_file = loadmat(os.path.join(base_path, 'groundtruth.mat'))

    camera_names = groundtruth_file['cameras']
    print(camera_names.keys())
    print('Identified {:d} cameras'.format(np.size(camera_names)))

    image_names = os.path.join(base_path, 'images', depth, str(camera_names[0]), '*.png')
    print(image_names)

load_multicam('easy_pose', 'train', 3, "jim")
