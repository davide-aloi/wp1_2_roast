# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:35:07 2022

@author: Davide Aloi - PhD student
"""

import glob
import numpy as np
from nilearn import image, plotting
from nilearn.image import new_img_like


path = 'D:\\roast-chapter3\wp2a\sub-03'
s1_v = glob.glob(path+ '/swsub-*_T1_*_emag.nii')


s1_t1 = glob.glob(path+ '/c1c2bin.nii')

s1_t1_map = image.load_img(s1_t1)

s1_v_map = image.load_img(s1_v)

s1_t1_data = s1_t1_map.get_fdata()
s1_v_data = s1_v_map.get_fdata()


mesh = np.where(s1_t1_data > 0,s1_v_data,0)

mesh_map = new_img_like(s1_t1_map,mesh)

plotting.plot_img(s1_v_map, cmap = 'cold_hot')
plotting.plot_img(s1_t1_map)

#image.math_img("img", img=mesh_map).to_filename('meshed.nii')
