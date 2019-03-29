from get_ref import *
import os

def load_multicam(dataset, group_name, section_number, optional_frames=None):
    home_path = get_ref(dataset)

    depth = 'depthRender'
    classes = 'groundtruth'
    file_format = 'mayaProject.{:06d}.png'
    base_path = os.path.join(home_path, group_name, str(section_number))
    print(base_path)

load_multicam('easy_pose', 'train', 3, "jim")
