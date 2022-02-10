% Author: Davide Aloi - PhD student - University of Birmingham
% Script to run roast simulation for Wp1a (1mA anodal on left M1, cathodal on right orbitofrontal cortex)

data_path = '/projects/chbh00025/wp1a_roast/'; % Main folder

%List of Wp1a participants
participants = {'03','04','05','07','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'}


%Running roast simulations for all wp1a participants with t1 and t2
for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = fullfile(folder, 'T1.nii')
    %t2 = dir(fullfile(folder, 't2*.nii'))
    %t2 = fullfile(t2.folder, t2.name)
    roast(t1, {'custom1', 1.0,'custom2', -1.0}, 'electype', 'pad', 'elecsize', [50 50 3])
    close all % necessary to free some RAM
end

