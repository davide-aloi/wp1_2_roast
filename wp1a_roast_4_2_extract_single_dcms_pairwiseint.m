% Author: Davide Aloi - PhD student - University of Birmingham

% The script extracts EP values for each subject, for the pairwise interaction (as, ac and cs).
% NB: the reason why I extract these values is because the PEB file is quite heavy
% (20MB) and it takes ages to load it in python.

cd C:\Users\davide\Documents\GitHub\wp1_2_roast\wp1a_DCMfiles\

load('PEB_pairwiseintA.mat')
ALLEP = {}

for i = 1:length(PEB_pairwiseint)
    thisEPVals = PEB_pairwiseint{i,1}.Ep(17:32,2)
    ALLEP{i} = thisEPVals
end

% This file contains 63 EP matrices, in the order as per above
save('wp1a_all_EPvalues_pairwiseint.mat','ALLEP')
