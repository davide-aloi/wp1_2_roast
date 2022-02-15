% Author: Davide Aloi - PhD student - University of Birmingham
% Script to run roast simulation for Wp2a (1mA anodal on left M1, cathodal on right orbitofrontal cortex)
% Update 02/02/2022 I'm trying to see if using manual coordinates works
% better

data_path = 'D:\roast-chapter3\wp2a\'; % Main folder

%List of Wp2a participants that have both a T1 and a T2
participants = {'01','02','03','04','06','07','08','09','10','11','12','13','14','15','17','18','19','20','22','23','24'}
participants = {'01'}

%List of participants with only t1
participants_onlyt1 = {'16'}
participants_onlyt1 = {}

%Running roast simulations for all wp2a participants with t1 and t2
for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = fullfile(folder, strcat('T1_cleaned.nii'))
    t2 = dir(fullfile(folder, 't2*_withoutcdl.nii'))
    t2found = size(t2)
    
    if t2found(1) == 0
        t2 = dir(fullfile(folder, 't2*.nii'))
    end
    
    t2 = fullfile(t2.folder, t2.name)
    roast(t1, {'custom1', 1.0,'custom2', -1.0}, 'T2', t2, 'electype', 'pad', 'elecsize', [50 50 3])
    close all % necessary to free some RAM
end

%Running roast simulations for wp2a participants with t1 only
for i = 1:length(participants_onlyt1)
    p = participants_onlyt1{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = fullfile(folder, strcat('T1_cleaned.nii'))
    roast(t1, {'custom1', 1.0,'custom2', -1.0}, 'electype', 'pad', 'elecsize', [50 50 3])
    close all % necessary to free some RAM
end
