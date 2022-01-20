"""
@author: Davide Aloi - PhD student - University of Birmingham

Script to rename wp2a files for the roast analysis

Output folder structure should be:

\main_folder
    \sub-01
    \sub-02
    ...
    \sub-x
        sub-x_T1.nii
        t2_.. .nii

"""

import os
main_folder = 'D:/roast-chapter3/wp2a/'

for subdir, dirs, files in os.walk(main_folder):
    if 'sub' in subdir: # iterating subjects' folders
        sub = subdir.split('-')[2] # subject number
        print(sub)
        os.chdir(subdir)
        for file in files:
                print(os.path.join(subdir, file))
                if '.json' in file:
                    os.rename(file,'sub-' + sub + '_T1.json')
                else:
                    if 'T1' in file:
                        os.rename(file,'sub-' + sub + '_T1.nii')
