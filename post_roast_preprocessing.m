clear all
% data_path = '/home/people/lxa512/roast-3.0/M1a/'; % this is the path to your dataset
data_path = 'D:\roast-chapter3\wp2a\';

% listof subjects
%participants = {'sub-01','sub-02','sub-03','sub-04','sub-06','sub-07','sub-08','sub-09','sub-10','sub-11','sub-12','sub-13','sub-14','sub-15','sub-17','sub-18','sub-19','sub-20','sub-22','sub-23','sub-24'}
participants = {'sub-01'}

nrun = length(participants); % this calculates the number of runs automatically
jobfile = {'C:\Users\davide\Documents\GitHub\wp1_2_roast\post_roast_preprocessing_job.m'};
jobs = repmat(jobfile, 1, nrun);
inputs = cell(4, nrun);

% the below now creates a loop to find all the necessary inputs for all the participants above

for crun = 1:nrun
    p = participants{crun}
    thisparticipantpath = fullfile(data_path,p);
    inputs{1, crun} = {thisparticipantpath}; % Change Directory: Directory - cfg_files
    %inputs{2, crun} = cellstr(spm_select('FPList', fullfile(thisparticipantpath, strcat(p,'_T1.nii')))); % Normalise: Estimate & Write: Image to Align - cfg_files. % This is your T1 (it's important that the estimation of the normalisation parameters is done with this image and not the emag or others)  
    inputs{2,crun} = cellstr(fullfile(thisparticipantpath,strcat(p,'_T1.nii')));
    
    write_im_names{1,1} = fullfile(thisparticipantpath,strcat(p,'_T1.nii'));
    tmp_emag = dir(fullfile(thisparticipantpath,strcat(p,'*emag.nii')));
    write_im_names{2,1} = fullfile(tmp_emag.folder,tmp_emag.name); 
    inputs{3, crun} = write_im_names; % Normalise: Estimate & Write: Images to Write - cfg_files % This is the emag and the T1 and are the ones that will be smoothed
    
    tmp_c1 = dir(fullfile(thisparticipantpath,strcat('c1*T1andT2.nii'))); %Nb for subjects that only had the t1 change T1andT2 to T1orT2 (i.e. subj 16)
    tmp_c2 = dir(fullfile(thisparticipantpath,strcat('c2*T1andT2.nii')));
    c_masks_names{1,1} = fullfile(tmp_c1.folder,tmp_c1.name);
    c_masks_names{2,1} = fullfile(tmp_c2.folder,tmp_c2.name);
    inputs{4, crun} = c_masks_names; % Normalise: Write: Images to Write - cfg_files % these are the c1 and c2 which will not be smoothed
end

spm('defaults', 'FMRI');
spm_jobman('run', jobs, inputs{:});
