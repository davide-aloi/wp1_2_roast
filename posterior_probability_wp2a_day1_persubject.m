
% Aloi Davide - UoB

% Calculate BMAs per subject (pre < post)

load PEBppA.mat

BMAs = {}

for i = 1:3:66
   this_subject_BMA = spm_dcm_peb_bmc(PEBpp{i})
   BMAs{end+1} = this_subject_BMA
end
BMAs = BMAs.'
save('Day1_all_Pp.mat','BMAs')