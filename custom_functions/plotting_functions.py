# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:53:48 2022

@author: davide
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from nilearn import image, plotting
from nilearn.image import new_img_like
import glob, os

main_folder = 'C:\\Users\\davide\\Documents\\GitHub\\wp1_2_roast\\' 
path = 'D:\\roast-chapter3\\wp2a_copy\\sub-01'

e_v = image.load_img(glob.glob(path + '/wsub-*_T1_*_e.nii'))
emag = image.load_img(glob.glob(path + '/wsub-*_T1_*_emag.nii'))
scan_shape = emag.get_fdata().shape[0:3] 
mni = image.load_img(os.path.join(main_folder, 'rois', 'MNI152_T1_1mm_Brain.nii'))
mni_resampled= image.resample_to_img(mni, emag, interpolation = 'nearest')

emag_data = emag.get_fdata().reshape(scan_shape) # Data with 4th dimention in the array dropped
emag_map = new_img_like(emag, emag_data) #  Restoring the data into a nibabel object

mask_data = image.load_img(glob.glob(path + '/wsub-*T1*T2_masks.nii')).get_fdata()
mask = new_img_like(emag_map, mask_data.reshape(scan_shape)) # Data with 4th dimention in the array dropped

mask_touched = image.math_img("(np.where(np.isin(img, np.arange(1, 4)), img, 0))*np.where(img2 !=0, 1,0)",
                              img = mask,
                              img2 = mni_resampled)



plt.imshow(np.rot90(mask_touched.get_fdata()[:,:,100]), cmap=plt.get_cmap('Paired'))



from nilearn.image import resample_img

v = emag_map.get_fdata()[:,:,100]
v = np.rot90(np.flip(v,1),3)

x = np.copy(np.rot90(np.flip(e_v.get_fdata()[:,:,100,0],1),3))
y = np.copy(np.rot90(np.flip(e_v.get_fdata()[:,:,100,1],1),3))

idxs = np.zeros(x.ravel().size, bool)
idxs[::15] = 1

idxs = np.where((v.ravel() > 0.1) & (idxs == 1), 1, 0)


idxs = idxs.reshape(x.shape)

x2 = np.where(idxs == 1, x, np.nan)
y2 = np.where(idxs == 1, y, np.nan)


plt.imshow(v, cmap=plt.get_cmap('jet'), vmin=0.0001, vmax=0.35)


plt.quiver(x2, y2)

plt.show()

