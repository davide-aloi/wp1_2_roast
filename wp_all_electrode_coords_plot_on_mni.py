# Author: Davide Aloi - PhD student - University of Birmingham
# Electrode coordinates plotted over MNI brain.

import numpy as np
import glob
import nilearn
from nilearn import image
import matplotlib.pyplot as plt


## Parameters and variables: 
mni_path = 'C:\\Users\\davide\\Documents\\GitHub\\wp1_2_roast\\rois\\MNI152_T1_1mm_Brain.nii'
coords_folder = 'C:\\Users\\davide\\Documents\\GitHub\\wp1_2_roast\\electrode_coords\\'

# Datasets names and subjects lists
db_names = ['wp2a','wp1a','wp1b']

