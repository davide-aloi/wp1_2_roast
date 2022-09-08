% Author: Davide Aloi - PhD student - University of Birmingham
% The script extracts EP values for each subject, for the pairwise
% comparison Anodal vs Sham (day1 pre vs day5 post)
cd C:\Users\davide\Documents\GitHub\wp1_2_roast\wp2a_DCMfiles\

load('PEBday1pre_day5post_AS_CS_AC_A.mat')

% NB the file contains 66 structures. These are related to 22 subjects and
% the 6 pairwise comparisons (Day 1 pre vs day5 post Anod vs sham, anod vs cath, cath vs sham
ALLEP = {}

for i = 1:length(PEBpairwise)
    thisEPVals = PEBpairwise{i,1}.Ep(17:32,2)
    ALLEP{i} = thisEPVals
end

% This file contains 66 EP matrices, in the order as per above
save('wp2a_all_EPvalues_pairwiseint_day1prevsday5post.mat','ALLEP')