% Author: Davide Aloi - PhD student - University of Birmingham
% The script extracts EP values for each subject, for the pairwise
% comparison Anodal vs Sham (day1)
cd C:\Users\davide\Documents\GitHub\wp1_2_roast\wp2a_DCMfiles\

load('PEB_pairwiseintA.mat')

% NB the file contains 132 structures. These are related to 22 subjects and
% the 6 pairwise comparisons
% order: day1 anodal vs sham, day5 anodal vs sham
% day 1 anodal vs cath, day 5 anodal vs cath
% day 1 cath vs sham, day 5 cath vs sham

ALLEP = {}

for i = 1:length(PEB_pairwiseint)
    thisEPVals = PEB_pairwiseint{i,1}.Ep(end-15:end,2)
    ALLEP{i} = thisEPVals
end

% This file contains 132 EP matrices, in the order as per above
save('wp2a_all_EPvalues_pairwiseint.mat','ALLEP')
