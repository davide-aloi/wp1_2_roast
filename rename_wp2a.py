"""
Created on Tue Jan  4 11:38:41 2022

@author: Davide Aloi PhD student

Script to rename Wp2a files for the roast analysis
"""

import os
main_folder = 'D:/roast-chapter3/wp2a/'

for subdir, dirs, files in os.walk(main_folder):
    if 'sub' in subdir: # iterating subjects' folders
        sub = subdir.split('-')[2] # subject number
        if sub != '01': # I had already renamed sub-01's files manually
            print (sub)
            os.chdir(subdir)
            for file in files:
                    print (os.path.join(subdir, file))
                    if sub == '03':
                        if '.json' in file:
                            os.rename(file,'sub-'+sub+'_T1.json')
                        else:
                            if 'T1' in file:
                                os.rename(file,'sub-'+sub+'_T1.nii')
                            if 't2' in file:
                                os.rename(file,'sub-'+sub+'_T2.nii')
                            