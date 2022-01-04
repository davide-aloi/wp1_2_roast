% Script to run roast simulation for wp2a. Aloi Davide
data_path = 'D:\roast-chapter3\wp2a\';

%List of Wp2a participants that have both a T1 and a T2
%participants = {'01','02','03','04','06','07','08','09','10','11','12','13','14','15','17','18','19','20','22','23','24'}
participants = {'01','02'} 

participants_onlyt2 = {'16'}

for i = 1:length(participants)
    p = participants{i}
    folder = fullfile(data_path,strcat('sub-',p))
    t1 = fullfile(folder,strcat('sub-',p,'_T1.nii'))
    t2 = fullfile(folder,strcat('sub-',p,'_T2.nii'))
    roast(t1,{'C3',1.0,'Fp2',-1.0},'T2',t2,'electype', 'pad', 'elecsize',[50 50 3],'capType','1020')
end


for i = 1:length(participants_onlyt2)
    p = participants_onlyt2{i}
    folder = fullfile(data_path,strcat('sub-',p))
    t1 = fullfile(folder,strcat('sub-',p,'_T1.nii'))
    roast(t1,{'C3',1.0,'Fp2',-1.0},'electype', 'pad', 'elecsize',[50 50 3],'capType','1020')
end

