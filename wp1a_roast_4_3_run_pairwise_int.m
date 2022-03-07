%% 3 PEBs coding for the interaction a>s a>c and c>s for wp1a.
clearvars;
cd C:\Users\davide\Documents\GitHub\wp1_2_roast\wp1a_DCMfiles

% field
field = {'A'
         %'B'
         }; 

%% Settings for PEB 2nd level
M = struct();
M.Q     = 'all';
M.Xnames = {'constant', 'A>S'};
M.X(:,1)=[1 1];
M.X(:,2)= [1 -1];
M.maxit = 256; % convergence before max num of iterations is reached


%% Loop
N = 21*3; %n of sessions = n participants * 3

for fi = 1:length(field)

    PEB = load(strcat('PEBpp',field{fi},'.mat'))
    
    PEB_pairwiseint={}; %PEB pairwise int
    
    PEBanodal = PEB.PEBpp(sort([1:3:N]));
    PEBcath = PEB.PEBpp(sort([2:3:N]));
    PEBsham = PEB.PEBpp(sort([3:3:N]));

    
    for i = 1:N/3
        
        M.Xnames = {'constant', 'A>S'};
        AS = [{PEBanodal{i}};{PEBsham{i}}]
        [PEB_pairwiseint{end+1}] = spm_dcm_peb(AS,M,field(fi)); %anodal vs sham
        
        M.Xnames = {'constant', 'A>C'};
        AC = [{PEBanodal{i}};{PEBcath{i}}]
        [PEB_pairwiseint{end+1}] = spm_dcm_peb(AC,M,field(fi)); %anodal vs cathodal
        
        M.Xnames = {'constant', 'C>S'};
        CS = [{PEBcath{i}};{PEBsham{i}}]
        [PEB_pairwiseint{end+1}] = spm_dcm_peb(CS,M,field(fi)); %cath vs sham
        

    end
    
    PEB_pairwiseint = PEB_pairwiseint'
    save(strcat('PEB_pairwiseint',field{fi}),'PEB_pairwiseint');

end
