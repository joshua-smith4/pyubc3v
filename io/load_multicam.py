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

    cameras = groundtruth_file['cameras']
    camera_names = [cameras[0][0][i][0][0][-1][0] for i in range(len(cameras[0][0]))]
    camera_names.reverse()
    print('Identified {:d} cameras'.format(len(camera_names)))

    image_folder_path = os.path.join(base_path, 'images', depth, str(camera_names[0]))
    image_names = [f for f in os.listdir(image_folder_path) if f.endswith('.png')]

    print(image_names)

load_multicam('easy_pose', 'train', 3, "jim")
