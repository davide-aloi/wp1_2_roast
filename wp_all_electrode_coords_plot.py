# Author: Davide Aloi - PhD student - University of Birmingham
# Electrode coordinates plots.

from nilearn import image
import numpy as np
from nilearn import plotting
from nilearn.image import new_img_like
from tqdm import tqdm
import os

## Parameters and variables: 
nyh_path = 'C:\\Users\\davide\\Desktop\\MRI TOOLS\\nyh\\skin.nii'
coords_folder = 'C:\\Users\\davide\\Documents\\GitHub\\wp1_2_roast\\electrode_coords\\'

# Datasets names and subjects lists
db_names = ['wp2a','wp1a', 'wp1b']


# Function to convert coordinates from MNI to matrix space
def mni_to_matrix(mni_coords, T):
    first_arg = np.transpose(np.linalg.inv(T))
    second_arg = (np.array([mni_coords[0],mni_coords[1],mni_coords[2], 1]))
    mat_coord = np.dot(second_arg,first_arg)
    mat_coord = mat_coord[0:3]
    mat_coord = np.round(mat_coord[:])

    return mat_coord

# LOAD new york head template (skin)
nyh = image.load_img(nyh_path)
nyh_data = nyh.get_fdata()
# Creating a surface of nyh
import skimage
from skimage import measure
from tqdm import tqdm
from scipy import ndimage

masked_nyh = np.zeros(nyh_data.shape)
nyh_data = nyh_data.astype(int)
for slice in range(0, nyh_data.shape[2]-1):
    x = nyh_data[:,:, slice].copy()
    xb = ndimage.binary_erosion(x).astype(int)
    xcont = np.where(x != xb, 1, 0)
    lab = measure.label(xcont)
    masked_nyh[:,:,slice] = np.where(lab == 1, 1, 0)

masked_nyh_img = new_img_like(nyh, masked_nyh)
#masked_nyh_img.to_filename('nyh_only_surface.nii')

nyh_x, nyh_y, nyh_z = np.where(masked_nyh==1)
all_indices = []
from scipy import spatial
for i in range(0,len(nyh_x)-1):
    all_indices.append([nyh_x[i],nyh_y[i],nyh_z[i]])
tree = spatial.KDTree(all_indices)

# Loading mni coordinates related to the electrodes (these are two dictionaries per 
# dataset (anod and cath))
for db_id, db in enumerate(db_names):
    mask_anod = np.zeros(nyh_data.shape)
    mask_cath = np.zeros(nyh_data.shape)
    distance = np.zeros(nyh_data.shape)

    size = nyh_data.shape

    # Loading elect coords
    anod = np.load(coords_folder + db + '_anod_mni_coords.npy', allow_pickle = True)
    anod = dict(enumerate(anod.flatten(), 1))[1]
    cath = np.load(coords_folder + db + '_cath_mni_coords.npy', allow_pickle = True)
    cath = dict(enumerate(cath.flatten(), 1))[1]

 
    for sub in tqdm(anod):
        center = mni_to_matrix(anod[sub][0], nyh.affine)
        closest_point_nyh = all_indices[tree.query(center)[1]]
        center =  closest_point_nyh
        distance = np.linalg.norm(np.subtract(np.indices(size).T,np.asarray(center)), axis=len(center))
        mask_anod += np.where(distance.T < 5, 1, 0)

    for sub in tqdm(cath):
        center = mni_to_matrix(cath[sub][0], nyh.affine)
        closest_point_nyh = all_indices[tree.query(center)[1]]
        center =  closest_point_nyh
        distance = np.linalg.norm(np.subtract(np.indices(size).T,np.asarray(center)), axis=len(center))
        mask_cath += np.where(distance.T < 5, 1, 0)

    mask_anod = np.where(mask_anod > 0, 1, 0)
    mask_cath = np.where(mask_cath > 0, 2, 0)

    mask = new_img_like(nyh, mask_anod + mask_cath)
    fname = db + "_manual_elect.nii"
    mask.to_filename(os.path.join('D:\\roast-chapter3\\wp_all_elec_locations\\',fname))


# Center of all points
for db_id, db in enumerate(db_names):
    # Loading elect coords
    print(db)
       
    mask = np.zeros(nyh_data.shape)
    size = nyh_data.shape

    anod = np.load(coords_folder + db + '_anod_mni_coords.npy', allow_pickle = True)
    anod = dict(enumerate(anod.flatten(), 1))[1]
    cath = np.load(coords_folder + db + '_cath_mni_coords.npy', allow_pickle = True)
    cath = dict(enumerate(cath.flatten(), 1))[1]

    anodnp = np.array(list(anod.values()))
    cathnp = np.array(list(cath.values()))
    distance = np.zeros(nyh_data.shape)

    # Anodal 
    medianx = np.median(anodnp[:, 0, 0])
    mediany = np.median(anodnp[:, 0, 1])
    medianz = np.median(anodnp[:, 0, 2])
    center = mni_to_matrix([medianx, mediany, medianz], nyh.affine)

    max_dist = 0
    for point in anodnp:
        point = mni_to_matrix(point[0], nyh.affine)
        dist = np.linalg.norm(center-point)
        if max_dist < dist:
            max_dist = dist

    print('max dist anod: ' + str(max_dist))
    distance = np.linalg.norm(np.subtract(np.indices(size).T,np.asarray(center)), axis=len(center))
    mask =  np.where((distance.T < max_dist) & (masked_nyh != 0), 1, mask)

   # Cathodal
    medianx = np.median(cathnp[:, 0, 0])
    mediany = np.median(cathnp[:, 0, 1])
    medianz = np.median(cathnp[:, 0, 2])
    center = mni_to_matrix([medianx, mediany, medianz], nyh.affine)

    max_dist = 0
    for point in cathnp:
        point = mni_to_matrix(point[0], nyh.affine)
        dist = np.linalg.norm(center-point)
        if max_dist < dist:
            max_dist = dist
    print('max dist cath: ' + str(max_dist))
    distance = np.linalg.norm(np.subtract(np.indices(size).T,np.asarray(center)), axis=len(center))
    mask =  np.where((distance.T < max_dist) & (masked_nyh != 0), 2, mask)
 
    # Saving res
    mask = new_img_like(nyh, mask)
    fname = db + "_area_all_points.nii"
    mask.to_filename(os.path.join('D:\\roast-chapter3\\wp_all_elec_locations\\',fname))
