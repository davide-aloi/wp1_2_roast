% Author: Davide Aloi - PhD student - University of Birmingham
% Script adapted from Luke Andrews' script, written for his MsC thesis.  
% The script normalises and resamples the anatomical scan, masks, emag and e maps for each subject (output suffix: w).
% The script also smooths every file with a FHWM filter (kernel: 4mm) (output suffix sw)
% Finally, the script creates a binary map containing white and grey matter only (c1c2bin.nii) (not used)

data_path = 'D:\roast-chapter3\wp2a\'; %path to wp2a roast simulations

% listof subjects
participants = {'sub-01','sub-02','sub-03','sub-04','sub-06','sub-07','sub-08','sub-09','sub-10','sub-11','sub-12','sub-13','sub-14','sub-15','sub-17','sub-18','sub-19','sub-20','sub-22','sub-23','sub-24'}
participants = {'sub-17'}

nrun = length(participants); % this calculates the number of runs automatically
jobfile = {'C:\Users\davide\Documents\GitHub\wp1_2_roast\wp2a_roast_3_post_roast_preprocessing_job.m'};
jobs = repmat(jobfile, 1, nrun);
inputs = cell(4, nrun);

% the below now creates a loop to find all the necessary inputs for all the participants above

for crun = 1:nrun
    p = participants{crun}
    thisparticipantpath = fullfile(data_path,p);
    inputs{1, crun} = {thisparticipantpath}; % Change Directory: Directory - cfg_files
    
    % Normalise: Estimate & Write: Image to Align - cfg_files. 
    % This is your T1 (Luke Andrews: it's important that the estimation of the normalisation parameters is
    % done with this image and not the emag or others)
    inputs{2,crun} = cellstr(fullfile(thisparticipantpath,'T1_cleaned.nii'));

    % Loading all the other scans and storing them in write_im_names
    % Loading anatomical scan (T1)
    write_im_names{1,1} = fullfile(thisparticipantpath,'T1_cleaned.nii'); %anat scan

    % Loading electric field map (magnitude)
    tmp_emag = dir(fullfile(thisparticipantpath,'T1_cleaned*emag.nii'));
    write_im_names{2,1} = fullfile(tmp_emag.folder,tmp_emag.name);
    
    % Loading electric field map (vector) 
    tmp_e = dir(fullfile(thisparticipantpath,'T1_cleaned*e.nii'));
    write_im_names{3,1} = fullfile(tmp_e.folder,tmp_e.name);

    % Loading all masks (c1...c6)
    for i = 1:6
        tmp_seg = dir(fullfile(thisparticipantpath,strcat('c',string(i),'*T1*T2.nii')));
        write_im_names{3+i,1} = fullfile(tmp_seg.folder,tmp_seg.name);
    end
    
    % Loading ROAST touched mask file (i.e. SPM masks binarised and
    % corrected with morphological operations and heuristics to remove remaining holes)
    all_masks_touched = dir(fullfile(thisparticipantpath,'T1_cleaned_T1*T2_masks.nii'));
    write_im_names{10,1} = fullfile(all_masks_touched.folder, all_masks_touched.name)
    
    % Emag, E-field, T1 and all the masks will also be smoothed (4mm FHWM)
    inputs{3, crun} = write_im_names; % Normalise: Estimate & Write: Images to Write - cfg_files

    % White and grey matter masks, as outputted from SPM, will be binarised
    % and saved. 
    tmp_c1 = dir(fullfile(thisparticipantpath,strcat('c1*T1*T2.nii')));
    tmp_c2 = dir(fullfile(thisparticipantpath,strcat('c2*T1*T2.nii')));
    c_masks_names{1,1} = fullfile(tmp_c1.folder,tmp_c1.name);
    c_masks_names{2,1} = fullfile(tmp_c2.folder,tmp_c2.name);
    inputs{4, crun} = c_masks_names; % Normalise: Write: Images to Write - cfg_files
end

spm('defaults', 'FMRI');
spm_jobman('run', jobs, inputs{:});
