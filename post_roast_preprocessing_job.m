%-----------------------------------------------------------------------
% Job saved on 15-Jul-2020 20:15:10 by cfg_util (rev $Rev: 6942 $)
% spm SPM - SPM12 (7219)
% cfg_basicio BasicIO - Unknown
%-----------------------------------------------------------------------
matlabbatch{1}.cfg_basicio.file_dir.dir_ops.cfg_cd.dir = '<UNDEFINED>';
matlabbatch{2}.spm.spatial.normalise.estwrite.subj.vol = '<UNDEFINED>';
matlabbatch{2}.spm.spatial.normalise.estwrite.subj.resample = '<UNDEFINED>';
matlabbatch{2}.spm.spatial.normalise.estwrite.eoptions.biasreg = 0.0001;
matlabbatch{2}.spm.spatial.normalise.estwrite.eoptions.biasfwhm = 60;
matlabbatch{2}.spm.spatial.normalise.estwrite.eoptions.tpm = {'C:\Users\davide\Documents\MATLAB\spm12\tpm\TPM.nii'};
matlabbatch{2}.spm.spatial.normalise.estwrite.eoptions.affreg = 'mni';
matlabbatch{2}.spm.spatial.normalise.estwrite.eoptions.reg = [0 0.001 0.5 0.05 0.2];
matlabbatch{2}.spm.spatial.normalise.estwrite.eoptions.fwhm = 0;
matlabbatch{2}.spm.spatial.normalise.estwrite.eoptions.samp = 3;
matlabbatch{2}.spm.spatial.normalise.estwrite.woptions.bb = [-78 -112 -70
                                                             78 76 85];
matlabbatch{2}.spm.spatial.normalise.estwrite.woptions.vox = [1 1 1];
matlabbatch{2}.spm.spatial.normalise.estwrite.woptions.interp = 4;
matlabbatch{2}.spm.spatial.normalise.estwrite.woptions.prefix = 'w';
matlabbatch{3}.spm.spatial.normalise.write.subj.def(1) = cfg_dep('Normalise: Estimate & Write: Deformation (Subj 1)', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','def'));
matlabbatch{3}.spm.spatial.normalise.write.subj.resample = '<UNDEFINED>';
matlabbatch{3}.spm.spatial.normalise.write.woptions.bb = [-78 -112 -70
                                                          78 76 85];
matlabbatch{3}.spm.spatial.normalise.write.woptions.vox = [1 1 1];
matlabbatch{3}.spm.spatial.normalise.write.woptions.interp = 4;
matlabbatch{3}.spm.spatial.normalise.write.woptions.prefix = 'w';
matlabbatch{4}.spm.spatial.smooth.data(1) = cfg_dep('Normalise: Estimate & Write: Normalised Images (Subj 1)', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{4}.spm.spatial.smooth.fwhm = [4 4 4];
matlabbatch{4}.spm.spatial.smooth.dtype = 0;
matlabbatch{4}.spm.spatial.smooth.im = 0;
matlabbatch{4}.spm.spatial.smooth.prefix = 's';
matlabbatch{5}.spm.util.imcalc.input(1) = cfg_dep('Normalise: Write: Normalised Images (Subj 1)', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{5}.spm.util.imcalc.output = 'c1c2bin';
matlabbatch{5}.spm.util.imcalc.outdir = {''};
matlabbatch{5}.spm.util.imcalc.expression = '(i1+i2) > 0.1';
matlabbatch{5}.spm.util.imcalc.var = struct('name', {}, 'value', {});
matlabbatch{5}.spm.util.imcalc.options.dmtx = 0;
matlabbatch{5}.spm.util.imcalc.options.mask = 0;
matlabbatch{5}.spm.util.imcalc.options.interp = 1;
matlabbatch{5}.spm.util.imcalc.options.dtype = 4;
