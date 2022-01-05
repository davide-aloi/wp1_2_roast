# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:35:07 2022

@author: Davide Aloi - PhD student
"""

import glob
import numpy as np
from nilearn import image, plotting
from nilearn.image import new_img_like
import os

main_folder = 'C:\\Users\\davide\\Documents\\GitHub\\wp1_2_roast'
bck_img_map = image.load_img(os.path.join(main_folder, 'MNI152_T1_1mm_Brain.nii'))

subjects = ['01','02','03','04','06','07','09','10','11','12','13','14','15','16','17','18','19','20','22','23','24']

subjects = ['01']


path = 'D:\\roast-chapter3\wp2a\sub-01'
emag_path = glob.glob(path+ '/swsub-*_T1_*_emag.nii')

emag_map = image.load_img(emag_path)
emag_data = emag_map.get_fdata()

anat_path = glob.glob(path+ '/c1c2bin.nii') #binary file

anat_map = image.load_img(anat_path)
anat_data = anat_map.get_fdata()


mesh_map = new_img_like(s1_t1_map,mesh)

plotting.plot_img(s1_v_map, cmap = 'cold_hot')
plotting.plot_img(s1_t1_map)

#image.math_img("img", img=mesh_map).to_filename('meshed.nii')


import matplotlib.pyplot as plt
hist, bins = np.histogram(mesh, bins=50)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()