% Author: Davide Aloi - PhD student - University of Birmingham
% Script to run roast simulation for Wp2a (1mA anodal on left M1, cathodal on right orbitofrontal cortex)

data_path = 'D:\roast-chapter3\wp2a\'; % Main folder

%List of Wp2a participants that have both a T1 and a T2
participants = {'01','02','03','04','06','07','08','09','10','11','12','13','14','15','17','18','19','20','22','23','24'}

%List of participants with only t1
participants_onlyt2 = {'16'}

%Running roast simulations for all wp2a participants with t1 and t2
for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = fullfile(folder, strcat('sub-', p, '_T1.nii'))
    t2 = dir(fullfile(folder, 't2*.nii'))
    t2 = fullfile(t2.folder, t2.name)
    roast(t1, {'C3',1.0,'Fp2',-1.0}, 'T2', t2, 'electype', 'pad', 'elecsize', [50 50 3], 'capType', '1020')
    close all % necessary to free some RAM
end

%Running roast simulations for wp2a participants with t1 only
for i = 1:length(participants_onlyt2)
    p = participants_onlyt2{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = fullfile(folder, strcat('sub-', p, '_T1.nii'))
    roast(t1, {'C3', 1.0, 'Fp2', -1.0}, 'electype', 'pad', 'elecsize', [50 50 3], 'capType', '1020')
    close all % necessary to free some RAM
end
