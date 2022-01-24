% Davide Aloi - PhD student - University of Birmingham - Centre for Human
% Brain Health.

%% Content
% Script to run roast simulations for Wp1b  dataset (-1.85mA cathodal on right
% cerebellum, +1.85mA anodal over right buccinator muscle)

%% Updates
% 20/01/2022: I am now running roast using only T1s. Many Wp1b T2s have artefacts and
% mess up the segmentation (i.e. weird masks, failed segmentations).

%% Code

data_path = '/projects/chbh00025/wp1b_roast'; % Main folder

%List of Wp1b participants
participants = {'01','02','03','04','05','06','07','08','09','10','11','12','13','15','16','17','18','19','21','22','23'}

%% Roast settings:
% Anode over the right cheek (e239 in egi system)
% Cathode over right cerebellum (e157)
% Current: 1.85mA [pad size 50x50x3]

for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = dir(fullfile(folder, '*T1*.nii'))
    t1 = fullfile(t1.folder, t1.name)
    %t2 = dir(fullfile(folder, '*T2*.nii'))
    %t2 = fullfile(t2.folder, t2.name)
    %roast(t1, {'E239', 1.85,'E157', -1.85}, 'T2', t2, 'electype', 'pad', 'elecsize', [50 50 3], 'capType', 'egi')
    roast(t1, {'E239', 1.85,'E157', -1.85}, 'electype', 'pad', 'elecsize', [50 50 3], 'capType', 'egi')
    close all % necessary to free some RAM
end
