% Davide Aloi - PhD student - University of Birmingham - Centre for Human
% Brain Health.

%% Content
% Script to run roast simulations for Wp1b  dataset (-1.85mA cathodal on right
% cerebellum, +1.85mA anodal over right buccinator muscle)

%% Updates
% 20/01/2022: I am now running roast using only T1s. Many Wp1b T2s have artefacts and
% mess up the segmentation (i.e. weird masks, failed segmentations).

% Now using manual coordinates
%% Code

data_path = 'D:\roast-chapter3\wp1b\'; % Main folder

%List of Wp1b participants
participants = {'01','02','03','04','05','06','07','08','09','10','11','12','13','15','16','17','18','19','21','22','23'}

%% Roast settings:
% Anode over the right cheek (more or less --> e239 in egi system)
% Cathode over right cerebellum (more or less --> e157)
% Current: 1.85mA [pad size 50x50x3]

%Running roast simulations for all wp1a participants with t1 and t2
for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = dir(fullfile(folder, '*_ras.nii'))
    t1 = fullfile(t1.folder, t1.name)
    %roast(t1, {'custom1', 1.85,'custom2', -1.85}, 'electype', 'pad', 'elecsize', [50 50 3])
    close all % necessary to free some RAM
end


