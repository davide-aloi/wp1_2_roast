% Author: Davide Aloi - PhD student - University of Birmingham

% The script extracts EP values for each subject, for the contrast pre vs
% post stimulation (wp1a dataset).
% The data I'm interested in is in file PEB_preVsPost_wp1b_A (second set of
% EP values per participant / session (order = anod cathodal sham). 
% NB: the reason why I extract these values is because the PEB file is quite heavy
% (20MB) and it takes ages to load it in python.

cd C:\Users\davide\Documents\GitHub\wp1_2_roast\wp1a_DCMfiles\

load('PEB_preVsPost_wp1a_A.mat')
ALLEP = {}

for i = 1:length(PEBpp)
    thisEPVals = PEBpp{1,i}.Ep(:,2)
    ALLEP{i} = thisEPVals
end

% This file contains 63 EP matrices, in the order as per above
save('wp1a_all_EPvalues.mat','ALLEP')
