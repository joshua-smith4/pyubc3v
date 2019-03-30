from get_ref import *
import os
from scipy.io import loadmat
import numpy as np
import pandas

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
    # print('cameras[0]')
    # print(len(cameras[0]))
    # print(cameras[0])
    # print('cameras[0][0]')
    # print(len(cameras[0][0]))
    # print(cameras[0][0])
    # print('cameras[0][0][0]')
    # print(len(cameras[0][0][0]))
    # print(cameras[0][0][0])
    # print('cameras[0][0][0][0]')
    # print(len(cameras[0][0][0][0]))
    # print(cameras[0][0][0][0])
    # print('cameras[0][0][0][0][0]')
    # print(len(cameras[0][0][0][0][0]))
    # print(cameras[0][0][0][0][0])
    # print('cameras[0][0][0][0][0][0]')
    # print(len(cameras[0][0][0][0][0][0]))
    # print(cameras[0][0][0][0][0][0])
    # print('cameras[0][0][0][0][0][1]')
    # print(len(cameras[0][0][0][0][0][1]))
    # print(cameras[0][0][0][0][0][1])
    # print('cameras[0][0][0][0][0][0][0]')
    # print(len(cameras[0][0][0][0][0][0][0]))
    # print(cameras[0][0][0][0][0][0][0].shape)
    # print(cameras[0][0][0][0][0][0][0])
    # print('cameras[0][0][0][0][0][0][0][0]')
    # print(len(cameras[0][0][0][0][0][0][0][0]))
    # print(cameras[0][0][0][0][0][0][0][0].shape)
    # print(cameras[0][0][0][0][0][0][0][0])
    # print('cameras[0][0][0][0][0][0][0][0]')
    # print(len(cameras[0][0][0][0][0][0][0][0]))
    # print(cameras[0][0][0][0][0][0][0][0].shape)
    # print(cameras[0][0][0][0][0][0][0][0].dtype)
    # print(cameras[0][0][0][0][0][0][0][0])
    # print('cameras[0][0][0][0][0][0][0][0]["translate"]')
    # print(len(cameras[0][0][0][0][0][0][0][0]["translate"]))
    # print(cameras[0][0][0][0][0][0][0][0]["translate"].shape)
    # print(cameras[0][0][0][0][0][0][0][0]["translate"].dtype)
    # print(cameras[0][0][0][0][0][0][0][0]["translate"])
    # print('cameras[0][0][0][0][0][0][0][0]["rotate"]')
    # print(len(cameras[0][0][0][0][0][0][0][0]["rotate"]))
    # print(np.squeeze(cameras[0][0][0][0][0][0][0][0]["rotate"]).shape)
    # print(cameras[0][0][0][0][0][0][0][0]["rotate"].dtype)
    # a = np.squeeze(cameras[0][0][0][0][0][0][0][0]["rotate"])
    # print(a)
    print(cameras[0][0]['Cam1']['frames'])
    image_folder_path = os.path.join(base_path, 'images', depth, str(camera_names[0]))
    image_names = [f for f in os.listdir(image_folder_path) if f.endswith('.png')]
    print('\tExpecting {:d} frames'.format(len(image_names)))
    # image_names.sort()
    # print(image_names)
    if optional_frames is None:
        optional_frames = (0,len(image_names)-1)

    instances = []
    for i in range(optional_frames[0], optional_frames[1]+1):
        instances.append({})
        # instances[i].append({}) # camera name dictionary
        for j in range(len(camera_names)):
            instances[i][camera_name[j]] = {
                'translation': cameras[0][0][len(camera_names) - j - 1],
                'rotation': 2,
                'depth_image': 3,
                'class_image': 4,
            }
            # instances[i][camera_name[j]]['depth_image']['cdata'] = instances[i][camera_name[j]]['depth_image']['cdata'][:,:,0]
        # instances[i]['posture'] = groundtruth_file['joints'][i]
    return instances, a
    return a

a = load_multicam('easy_pose', 'train', 3)
