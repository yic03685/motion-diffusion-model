from Common.system.motion_file import MotionFile
from visualize import vis_utils

def render_smpl(smpl_file: MotionFile, device:int=0):
    npy2obj = vis_utils.npy2obj(smpl_file.get_data(), 0, 0, device=device, cuda=True)
    return npy2obj.save_npy()
