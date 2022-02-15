# Author: Davide Aloi - PhD student - University of Birmingham
# The script contains the coordinates for the electrodes in wp1b. The coordinates were 
# identified using MRIcronGL. The script also iterates through the folders and saves a file
# .txt named customLocations.txt containing the coordinates for the active and reference
# electrodes. 

import os 
main_folder = 'C:\\Users\\davide\\Documents\\GitHub\\wp1_2_roast\\' 
output_folder = 'D:\\roast-chapter3\\wp_all_results\\' # where to save results
data_folder = 'D:\\roast-chapter3\\'

# Datasets names and subjects lists
db_names = ['wp1b']
db_subjects = [['01','02','03','04','05','06','07','08','09','10','11','12','13','15','16','17','18','19','21','22','23']]

# List of coordinates for each subject (return electrode: cathodal, active electrode: anodal)
anod_coords = {
              '01': (152,168,54),
              '02': (155,182,64),
              '03': (155,178,55),
              '04': (150,183,50),
              '05': (143,178,67),
              '06': (152,171,32),
              '07': (147,180,70),
              '08': (154,171,49),
              '09': (153,169,64),
              '10': (146,190,67),
              '11': (156,183,49),
              '12': (149,186,67),
              '13': (154,185,49),
              '15': (162,198,52),
              '16': (142,187,75),
              '17': (158,184,56),
              '18': (160,190,40),
              '19': (154,179,52),
              '21': (145,161,70),
              '22': (147,184,67),
              '23': (151,181,37)
}

cath_coords = {
              '01': (118,49,94),
              '02': (118,51,112),
              '03': (123,42,114),
              '04': (116,43,124),
              '05': (131,47,103),
              '06': (133,53,85),
              '07': (126,51,115),
              '08': (143,54,74),
              '09': (121,48,92),
              '10': (128,41,87),
              '11': (126,49,93),
              '12': (133,38,87),
              '13': (134,47,100),
              '15': (143,40,91),
              '16': (122,49,108),
              '17': (139,53,97),
              '18': (133,52,85),
              '19': (132,57,92),
              '21': (129,47,90),
              '22': (129,58,84),
              '23': (140,54,106)            
            }


# Saving txt files with electrode coordinates.

for db_id, db in enumerate(db_names): # Iterate all three datasets
    db_path = os.path.join(data_folder, db) # Dataset folder

    for i, subject in enumerate(db_subjects[db_id]): #Iterate all subjects
        path = db_path + '\sub-' + subject # Subject folder
        print(path)
        fname = 'customLocations.txt'
        anod = anod_coords[subject]
        cath = cath_coords[subject]
        with open(path + '\\' + fname, 'w') as f:
            f.write('custom1 ' + str(anod[0]) + ' ' + str(anod[1]) + ' ' + str(anod[2]))
            f.writelines('\n')
            f.write('custom2 ' + str(cath[0]) + ' ' + str(cath[1]) + ' ' + str(cath[2]))




# MNI coordinates from affine matrix 
import numpy as np
def matrix_to_mni(matrix_coord, T):
    second_arg = np.array([matrix_coord[0],matrix_coord[1],matrix_coord[2], 1])
    second_arg = np.reshape(second_arg,[-1,1])
    mni_coord = np.dot(T,second_arg)
    return np.reshape(mni_coord[0:3],[1,-1])


from nilearn import image
import glob

anod_mni = anod_coords.copy()
cath_mni = cath_coords.copy()

for db_id, db in enumerate(db_names): # Iterate all three datasets
    db_path = os.path.join(data_folder, db) # Dataset folder

    for i, subject in enumerate(db_subjects[db_id]): #Iterate all subjects
        path = db_path + '\sub-' + subject # Subject folder
        print(path)
        path_to_scan = glob.glob(path + '\*T1_VOL_*_ras.nii')
        if not path_to_scan:
            path_to_scan = glob.glob(path + '\sub*ses-*_T1w_ras.nii')

        T1 = image.load_img(path_to_scan)

        anod = anod_coords[subject]
        cath = cath_coords[subject]
        anod_mni[subject] = matrix_to_mni(anod, T1.affine)
        cath_mni[subject] = matrix_to_mni(cath, T1.affine)


np.save('wp1b_anod_mni_coords.npy', anod_mni) 
np.save('wp1b_cath_mni_coords.npy', cath_mni) 
