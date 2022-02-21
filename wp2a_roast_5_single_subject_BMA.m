% Author: Davide Aloi - PhD student - University of Birmingham

% The script applies BMR and BMA on each subjects' PEB model (pre < post) to reduce connections that were not adding to the models evidence.
% This is done for all 3 stimulation modalities (anodal, cathodal and sham).


load wp2a_DCMfiles/PEB_preVsPostDay1.mat % File containing the 66 pre < post PEBs (one per subject x 3 stimulation modalities)

BMAs = {}

for i = 1:66
   this_subject_BMA = spm_dcm_peb_bmc(PEBpp{i})
   BMAs{end+1} = this_subject_BMA
end

save('Day1_all_Pp.mat','BMAs') % Saving the results.
