# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:53:48 2022

@author: Davide Aloi - PhD student - University of Birmingham
NB: Still have to add comments
"""

import glob, os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure



def roast_vector_sim(e: np.ndarray, e_mag: np.ndarray, mask: np.ndarray, vmin = 0,
                     vmax = 0.35, vmin_v = 0.1, vmax_v = 2, axis = 2, which_slice = 0,
                     subsample = 2, scale = 3, figsize = (30,30)):
    """
    Description:
        Plots results from electric field maps generated by ROAST, masked using a brain mask.

        Parameters
    ----------
    e : np.ndarray
        electric field vectors map.
    e_mag : np.ndarray
        electric field magnigute map.
    mask : np.ndarray
        Brain mask map. It should contain only 0 and 1. I will be used to mask the data.
    vmin : TYPE, optional
        vmin for electric field magnitude cmap. The default is 0.
    vmax : TYPE, optional
        vmax for electric field magnitude cmap. The default is 0.35.
    vmin_v : TYPE, optional
        vmin electric field vectors under this threshold won't be shown. The default is 0.1.
    vmax_v : TYPE, optional
        vmin electric field vectors above this threshold won't be shown. The default is 2.
    axis : TYPE, optional
        Which axis to plot. 0 = axial, 1 = coronal, 2 = sagittal. The default is 2.
    which_slice : TYPE, optional
        Slice of the scan to plot. The default is 0.
    subsample : TYPE, optional
        Removing vectors every N elements. It avoids overcrowded plots. The default is 2.
    scale : TYPE, optional
        Factor of scale for the vectors. Higher -> smaller vectors. The default is 3.
    figsize: int, optional
        size of the matplotlib plot

        Returns
     ----------
     matplotlib plot

    Raises
    ------
    Exception
        Scans should all have the same dimension.
        axis can only be 0, 1 or 2.
        which_slice should not exceed scan dimension on plotted plane.
    """


    if (e.shape[0:3] != mask.shape != mask.shape):
        raise Exception("Electric field map and mask should have the same dimension.")

    if not np.isin(axis, [0, 1, 2]):
        raise Exception("Invalid axis. Axis can only be equal to 0 (x) 1 (y) or 2 (z).")

    if e_mag.shape[axis] > which_slice:
        if axis == 0:
            e_mag = np.where(mask[which_slice, :, :] != 0, e_mag[which_slice, :, :], 0)
            x = -e[which_slice,:,:, 0]
            y = -e[which_slice,:,:, 1]

        if axis == 1:
            e_mag = np.where(mask[:, which_slice, :] != 0, e_mag[:, which_slice, :], 0)
            x = -e[:,which_slice,:, 0]
            y = -e[:,which_slice,:, 2]

        if axis == 2:
            e_mag = np.where(mask[:, :, which_slice] != 0, e_mag[:, :, which_slice], 0)
            x = -e[:,:,which_slice, 1]
            y = -e[:,:,which_slice, 2]

        idxs = np.zeros(x.ravel().size, bool)
        idxs[::subsample] = 1
        idxs = np.where(((e_mag.ravel() > vmin_v) & (e_mag.ravel() < vmax_v)) & (idxs == 1), 1, 0)
        idxs = idxs.reshape(x.shape)
        x = np.where(idxs == 1, x, np.nan)
        y = np.where(idxs == 1, y, np.nan)

        f, ax = plt.subplots(figsize=figsize)
        ax.imshow(e_mag, cmap=plt.get_cmap('jet'), vmin=vmin, vmax=vmax)
        ax.quiver(x, y, scale = scale,
                   minlength = 2,
                   headwidth = 3, headlength = 3, alpha = 0.7,
                   linewidth = 0.2)

        ax.axis('off')

        return ax

    else:
        raise Exception("Slice chosen exceeds scan dimension on chosen axis (" + str(axis) + ")\n"
                        "Scan shape: " + str(e_mag.shape) + "\n"
                        "Sclice chosen: " + str(which_slice))
