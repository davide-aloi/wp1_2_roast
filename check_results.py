# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:35:07 2022

@author: Davide Aloi - PhD student
"""

from nilearn import image, plotting
from nilearn.image import new_img_like

import os
import numpy as np

s1_v = os.path.join('D:\\roast-chapter3\wp2a\sub-01', 'swsub-01_T1_20220103T140836_emag.nii') 
s1_t1 = os.path.join('D:\\roast-chapter3\wp2a\sub-01', 'c1c2bin.nii')

s1_t1_map = image.load_img(s1_t1)

s1_v_map = image.load_img(s1_v)

s1_t1_data = s1_t1_map.get_fdata()
s1_v_data = s1_v_map.get_fdata()


mesh = np.where(s1_t1_data > 0,s1_v_data,0)

mesh_map = new_img_like(s1_t1_map,mesh)

plotting.plot_img(mesh_map)

image.math_img("img", img=mesh_map).to_filename('meshed.nii')
