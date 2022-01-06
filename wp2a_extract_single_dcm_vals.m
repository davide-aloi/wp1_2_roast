%Script to extract pre vs post EP values for each subject 
% I am going to use this to plot responders vs non responders EP values 
clear all
cd C:\Users\davide\Documents\GitHub\WP2A_joystick\PEB_nov2021\results_wp2a_pairwise_day1only\
load('PEBpairwise_day1A.mat')

ALLEP = {}

for i = 1:length(PEBpairwise_day1)
    thisEPVals = PEBpairwise_day1{i,1}.Ep(17:32)
    ALLEP{i} = thisEPVals
end

save('Day1_all_EPvalues.mat','ALLEP')


clear all
cd C:\Users\davide\Documents\GitHub\WP2A_joystick\friday_session\DCM_friday_session\results\PEBfullAB_all
load('PEBppA.mat')

ALLEP = {}

for i = 1:length(PEBpp)
    thisEPVals = PEBpp{i,1}.Ep(:,2)
    ALLEP{i} = thisEPVals
end

save('Day5_all_EPvalues.mat','ALLEP')