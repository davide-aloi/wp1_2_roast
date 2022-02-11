% Author: Davide Aloi - PhD student - University of Birmingham
% Wp1a T1s have some issues with the headers. Roast thinks they're not in
% RAS space, but they actually are. I therefore convert all the scans to
% RAS using roast function convertToRas.m. This way Roast won't change
% the electrode coordinates that I pass when running the simulations on
% wp1a. 

data_path = 'D:\roast-chapter3\wp1a\'; % Main folder

%List of Wp1a participants
participants = {'07','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'}

%Running roast simulations for all wp1a participants with t1 and t2
for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path, strcat('sub-', p))
    t1 = fullfile(folder, 'T1.nii')
    convertToRAS(t1)
end
