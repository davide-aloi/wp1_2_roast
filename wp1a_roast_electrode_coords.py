# Author: Davide Aloi - PhD student - University of Birmingham
# The script contains the coordinates for the electrodes in wp1a. The coordinates were 
# identified using MRIcronGL. The script also iterates through the folders and saves a file
# .txt named customLocations.txt containing the coordinates for the active and reference
# electrodes. 

import os 
main_folder = 'C:\\Users\\davide\\Documents\\GitHub\\wp1_2_roast\\' 
output_folder = 'D:\\roast-chapter3\\wp_all_results\\' # where to save results
data_folder = 'D:\\roast-chapter3\\'

# Datasets names and subjects lists
db_names = ['wp1a']
db_subjects = [['03','04','05','07','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']]

# List of coordinates for each subject (return electrode: cathodal, active electrode: anodal)
anod_coords = {
            '03': (36,117,204), # --> 163,131,175
            '04': (46,131,228),
            '05': (48,118,210),
            '07': (49,137,226),
            '09': (48,136,181),
            '10': (31,121,207),
            '11': (40,125,208),
            '12': (47,132,193),
            '13': (30,96,187),
            '14': (41,80,222),
            '15': (52,138,231),
            '16': (43,129,191),
            '17': (51,124,188),
            '18': (44,127,211),
            '19': (51,126,208),
            '20': (45,122,212),
            '21': (54,130,213),
            '22': (31,139,209),
            '23': (36,117,180),
            '24': (37,128,202),
            '25': (32,130,183),
            '26': (26,141,183)
}

cath_coords = {
            '03': (119,185,190),
            '04': (116,205,181),
            '05': (134,206,148),
            '07': (134,207,179),
            '09': (125,196,155),
            '10': (133,187,194),
            '11': (102,213,173),
            '12': (122,212,138),
            '13': (130,216,152),
            '14': (116,211,159),
            '15': (115,220,160),
            '16': (123,223,128),
            '17': (103,228,124),
            '18': (119,217,136),
            '19': (110,231,140),
            '20': (115,221,149),
            '21': (112,222,147),
            '22': (107,219,156),
            '23': (113,209,140),
            '24': (104,228,149),
            '25': (118,215,137),
            '26': (103,233,137)
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