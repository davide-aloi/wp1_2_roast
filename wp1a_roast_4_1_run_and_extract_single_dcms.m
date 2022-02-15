%% This script runs a PEB of pre < post within subject, for the wp1a dataset

% loading GCM struct with 126 DCMs (anod pre anod post, cath pre cath post,
% sham pre anod post x participant)
load('wp1a_DCMfiles/GCM_fullAB_all.mat')

%% Specify PEB model settings for 2nd level: pre < post in each individual
Mpp = struct();
Mpp.Q     = 'all';
Mpp.Xnames = {'constant', 'pre < post'};
Mpp.X(:,1)=[1 1];
Mpp.X(:,2)=[-1 1];
Mpp.maxit = 256; % convergence before max num of iterations is reached

n_gcms = length(GCM)

for thispp = 1:n_gcms/2
    GCM_temp = GCM(thispp : thispp + 1);
    [PEBpp{thispp}, GCMpp{thispp}] = spm_dcm_peb(GCM_temp, Mpp, 'A');
    thispp = thispp + 2
end

%PEB_preVsPost_wp1b.mat will contain 63 structs that are PEB (pre<post) for each
%participant, for polarities Sham, Cathodal and Anodal (in this order).

save(strcat('PEB_preVsPost_wp1b_', 'A'), 'GCMpp', 'PEBpp');

