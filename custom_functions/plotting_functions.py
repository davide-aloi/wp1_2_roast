# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:53:48 2022

@author: Davide Aloi
"""

import glob, os

import matplotlib.pyplot as plt
import numpy as np
from nilearn import image, plotting
from nilearn.image import new_img_like
from nilearn.image import resample_img


def roast_vector_sim(e: np.ndarray, e_mag: np.ndarray, mask: np.ndarray, vmin = 0, 
                     vmax = 0.35, vmin_v = 0.1, axis = 2, which_slice = 0, subsample = 2,
                     scale = 3): 

    if (e.shape[0:3] != mask.shape != mask.shape):
        raise Exception("Electric field map and mask should have the same dimension.")
    
    
    if not np.isin(axis, [0, 1, 2]):
        raise Exception("Invalid axis. Axis can only be equal to 0 (x) 1 (y) or 2 (z).")
    
    
    if e_mag.shape[axis] > which_slice:
        if axis == 0:
            e_mag = np.where(mask[which_slice, :, :] != 0, e_mag[which_slice, :, :], 0)
            e_mag = np.rot90(e_mag, 1)
            
            x = np.rot90(np.copy(e[which_slice,:,:, 0]),1)
            y = np.rot90(np.copy(e[which_slice,:,:, 1]),1)
            
        if axis == 1:
          e_mag = np.where(mask[:, which_slice, :] != 0, e_mag[:, which_slice, :], 0)
          e_mag = np.rot90(np.flip(e_mag, 1),3)
          
          x = np.rot90(np.flip(np.copy(e[:,which_slice,:, 0]), 1), 3)
          y = np.rot90(np.flip(np.copy(e[:,which_slice,:, 2]), 1), 3)
        

        if axis == 2:
            e_mag = np.where(mask[:, :, which_slice] != 0, e_mag[:, :, which_slice], 0)
            e_mag = np.rot90(np.flip(e_mag, 1), 3)

            x = np.copy(np.rot90(np.flip(e[:,:,which_slice, 1],1),3))
            y = np.copy(np.rot90(np.flip(e[:,:,which_slice, 2],1),3))
            
            
            
            
        idxs = np.zeros(x.ravel().size, bool)
        idxs[::subsample] = 1         
        idxs = np.where((e_mag.ravel() > vmin_v) & (idxs == 1), 1, 0)
        idxs = idxs.reshape(x.shape)
        x = np.where(idxs == 1, x, np.nan)
        yy = np.where(idxs == 1, y, np.nan)

        plt.imshow(e_mag, cmap=plt.get_cmap('jet'), vmin=vmin, vmax=vmax)
        plt.quiver(x, y, scale = scale, 
                   minlength = 2,
                   headwidth = 3, headlength = 3, alpha = 0.7,
                   linewidth = 0.2)
        plt.show() 
        
    else:
        raise Exception("Slice chosen exceeds scan dimension on chosen axis (" + str(axis) + ")\n" 
                        "Scan shape: " + str(e_mag.shape) + "\n"
                        "Sclice chosen: " + str(which_slice))   
        
          

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

mask_touched = image.math_img("np.where(img == 2, 1,0)",
                              img = mask_touched)

emag_map = image.smooth_img(emag_map, fwhm = 4)
e_v = image.smooth_img(e_v, fwhm = 4)

roast_vector_sim(e_v.get_fdata(), emag_map.get_fdata(), mask_touched.get_fdata(),
                 axis = 2,
                 vmin = 0, vmax = 0.16,
                 subsample = 20,
                 vmin_v = 0.02,
                 which_slice = 100,
                 scale = 3)


