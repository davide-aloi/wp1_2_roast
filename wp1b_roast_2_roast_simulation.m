% Davide Aloi - PhD student - University of Birmingham
% Script to run roast simulation for Wp1b (1.85mA cathodal on right cerebellum, cathodal over right buccinator muscle)

data_path = 'D:\roast-chapter3\wp1b\'; % Main folder

%List of Wp2a participants that have both a T1 and a T2
participants = {'01','02','03','04','05','06','07','08','09','10','11','12','13','15','16','17','18','19','20','21','22','23'}
participants = {'01','02'}

% Running roast simulations for all wp1b participants with t1 and t2
% Anode over the right cheek (e239 in egi system)
% Cathode over right cerebellum (e157)
for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = dir(fullfile(folder, '*T1*.nii'))
    t1 = fullfile(t1.folder, t1.name)
    t2 = dir(fullfile(folder, '*T2*.nii'))
    t2 = fullfile(t2.folder, t2.name)
    roast(t1, {'E239', 1.85,'E157', -1.85}, 'T2', t2, 'electype', 'pad', 'elecsize', [50 50 3], 'capType', 'egi')
    close all % necessary to free some RAM
end
