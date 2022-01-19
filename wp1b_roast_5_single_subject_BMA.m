% Aloi Davide - PhD student - University of Birmingham

% The script applies BMR and BMA on each subjects' PEB model (pre < post) to
% reduce connections that were not adding to the models evidence.
% Dataset: wp1b.
% This is done for all 3 stimulation modalities (sham, cathodal and anodal).

% File containing the 63 pre < post PEBs (one per subject x 3 stimulation modalities)
clear all
load wp1b_DCMfiles/PEB_preVsPost_wp1b_A.mat 
BMAs = {}

for i = 1:length(GCMpp)
   this_subject_BMA = spm_dcm_peb_bmc(PEBpp{i})
   BMAs{end+1} = this_subject_BMA
end

save('All_Pp_wp1b.mat','BMAs') % Saving the results.
