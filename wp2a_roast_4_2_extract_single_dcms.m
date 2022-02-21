% Author: Davide Aloi - PhD student - University of Birmingham

% The script extracts EP values for each subject, for the contrast pre vs post stimulation, Day-5 only.

cd C:\Users\davide\Documents\GitHub\wp1_2_roast\wp2a_DCMfiles\day_5\

load('PEB_preVsPostDay5.mat')
% NB the file contains 66 structures. These are related to 22 subjects and the 3 stimulation modalities (anodal, cathodal and sham, in this order)
% So the structure 1 is related to subject 1 (anodal), the structure 2 to subject 1 (cathodal) and the structure 3 to subject 1 (sham) and so on

ALLEP = {}

for i = 1:length(PEBpp)
    thisEPVals = PEBpp{i,1}.Ep(:,2)
    ALLEP{i} = thisEPVals
end

% This file contains 66 EP matrices, in the order as per above
save('Day5_all_EPvalues.mat','ALLEP')
