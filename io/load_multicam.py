from get_ref import *
import os
from scipy.io import loadmat
from scipy.misc import imread
import numpy as np
import pandas


def load_multicam(dataset, group_name, section_number, optional_frames=None):
    home_path = get_ref(dataset)

    depth = 'depthRender'
    classes = 'groundtruth'
    file_format = 'mayaProject.{idx:06d}.png'
    base_path = os.path.join(home_path, group_name, str(section_number))

    depth_path = os.path.join(
        base_path, 'images', depth, '{camera_name}', file_format)
    # print(depth_path.format(camera_name='Cam1', idx=25))
    class_path = os.path.join(
        base_path, 'images', classes, '{camera_name}', file_format)

    print('Loading groundtruth file {:d} ...'.format(section_number))
    groundtruth_file = loadmat(os.path.join(base_path, 'groundtruth.mat'))

    cameras = groundtruth_file['cameras']
    camera_names = [cameras[0][0][i][0][0][-1][0]
                    for i in range(len(cameras[0][0]))]
    camera_names.reverse()
    print('Identified {:d} cameras'.format(len(camera_names)))
    image_folder_path = os.path.join(
        base_path, 'images', depth, str(camera_names[0]))
    image_names = [f for f in os.listdir(
        image_folder_path) if f.endswith('.png')]
    print('\tExpecting {:d} frames'.format(len(image_names)))
    # image_names.sort()
    # print(image_names)
    if optional_frames is None:
        optional_frames = (0, len(image_names) - 1)

    instances = []
    for i in range(optional_frames[0], optional_frames[1] + 1):
        instances.append({})
        # instances[i].append({}) # camera name dictionary
        for camera_name in camera_names:
            instances[i][camera_name] = {
                'translation': cameras[0][0][camera_name]['frames'][0][0][0][i]['translate'][0][0][0],
                'rotation': cameras[0][0][camera_name]['frames'][0][0][0][i]['rotate'][0][0][0],
                'depth_image': imread(depth_path.format(camera_name=camera_name, idx=i+1)),
                'class_image': imread(class_path.format(camera_name=camera_name, idx=i+1)),
            }
        print(i)
            # instances[i][camera_name]['depth_image']['cdata'] = instances[i][camera_name[j]                                                             ]['depth_image']['cdata'][:, :, 0]
        # instances[i]['posture'] = groundtruth_file['joints'][i]
    # return instances
    return groundtruth_file, instances


a,b = load_multicam('easy_pose', 'train', 3)
