Aloi Davide - PhD Student (UoB)

Analysis of electric field magnitudes (wp2a dataset only at the moment) and correlation analysis with Dynamic Causal Modelling (DCM) results. 

The goal of these analyses is to establish whether there is a relationship between single-subject electric field (E-field) magnitudes generated with the [ROAST](https://github.com/andypotatohy/roast#5-outputs-of-roast-software) pipeline (Huang et al., 2019) and changes in effective connectivity within the motor network, derived using DCM and parametric empirical bayes (PEB). 

The two analyses are:
1) Correlation analysis between E-field magnitude - medians and max values - (or the current density?) in the motor cortex (M1) and Thalamus (Th) with self- / between-connectivities (M1 and Th only?) as derived from the DCM. e.g. Indahlastari et al. (2021). At the moment I am correlating e-field measures only with DCM measures derived from the contrast pre vs post Day-1 anodal only. However, I should also correlate those e-field measures with DCM measures derived from the contrast pre vs post Day-1 sham. I expect to find correlations between e-field measures and DCM measures for the anodal condition but not for sham. 
2) Pattern-recognition analysis using support vector machine (SVM) learning algorithm on MRI-derived tDCS current models to provide classification of tDCS treatment response (as reflected by increased M1-TH or TH-M1 connectivity or whatever other measure we decide). e.g. Albizu et al. (2020). The question here is: can we classify people who had an increase in thalamo-cortical connectivity  using features from the MRI-current models? 


The two analyses require similar preprocessing steps. Here's the list of the steps I've done and the respective scripts.

WP2A: I start from a dataset containing 22 folders (one per participant), each containing a T1 and a T2 scan (except for subject 16 who has only a T1). 

1) [Renaming of anatomical scans](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_roast_1_rename_scans.py): this renames the anatomical scans of each participant (i.e. sub-01_T1.nii etc). 
2) [ROAST simulations](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_roast_2_roast_simulation.m): this script runs the ROAST simulations. In brief, ROAST outputs the following scans for each subject, while also using SPM routines for tissue segmentation: Voltage ("subjName_simulationTag_v.nii", unit in mV), E-field ("subjName_simulationTag_e.nii", unit in V/m) and E-field magnitude ("subjName_simulationTag_emag.nii", unit in V/m).
The settings I have used for the simulation are: (t1, {'C3',1.0,'Fp2',-1.0},'T2', t2,'electype', 'pad', 'elecsize', [50 50 3], 'capType', '1020').
3) [Post ROAST preprocessing](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_roast_3_post_roast_preprocessing.m): ROAST outputs are in the ROAST model space. This script moves the results back to the MRI space, coregisters and normalises the electric field maps generated by ROAST. The script also normalise the T1 scan and all the masks. 
4) [Ep values extraction from PEB result](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_roast_4_extract_single_dcms.m) (Day-1 only): this script, starting from [this](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_DCMfiles/PEB_preVsPostDay1.mat) .mat structure containing 66 PEBs (1 per participant / polarity), extracts the Ep values for each participant. The resulting [file](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_DCMfiles/Day1_all_EPvalues.mat) contains 66 matrices (participant 1 anodal, cathodal and sham, participant 2 ... 22).
5) [Estimation of posterior probability](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_roast_5_single_subject_BMA.m) associated to each PEB extracted above. The script runs bayesian model averages for each PEB using the DCM function spm_dcm_peb_bmc. Results are saved in [this](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_DCMfiles/PEB_preVsPostDay1.mat) .mat structure and used later on in the analyses to exclude connections with a posterior probability lower than 75%. 
6) [WP2a e-magnitude measures estimation and correlation analysis](https://github.com/Davi93/wp1_2_roast/blob/main/wp2a_roast_6_data_analysis.ipynb).
Steps: 
   1) Load MNI template and M1/Th ROIs.
   2) Load .mat structure with Ep values and .mat structure with Pp values (Nb. Pp values are not used anymore); 
   3) For each subject: 
      1) Load normalised scan containing E-field magnitude (wsub-*_T1_*_emag.nii), normalised CSF, white and grey matter maps (wc1-2-3sub*.nii).
      2) Save DCM values related to the connections M1-M1, Th-Th, M1->Th and Th-> M1;
      3) Smooth E-field magnitude map using FWHM (4mm kernel); 
      4) Mask E-field magnitude map with MNI template to exclude values outside the brain (useless if I then mask with CSF, wm and gm maps or with the M1/Th ROIs);
      5) Mask E-field magnitude map with M1 and Th ROIs and estimate means, medians and max electric-field values within the two ROIs; 
      6) Save electric-field magnitude derived measures;
      7) Plot smoothed E-field magnitude map;
      8) Run 16 correlations: 4 DCM measures and 4 E-field measures (medians and max values).
      9) Plot correlations.

Questions: 
1) Electric field magnitudes or current densities? 
2) If so, how to deal with probabilistic masks?
3) Should I threshold WM masks and apply binary erosion to remove the overlap between WM and GM?
4) How to deal with Ep values which corresponding Pp is lower than our threshold (75%?)
5) Should I mask out CSF tissue? Should I use a binary map containing only WM and GM?
6) Hypotheses? Ideas?


Plots:
![Sticky note mind map - Sticky note mind map](https://user-images.githubusercontent.com/4202630/148744899-831ed72d-4f5a-4428-aa23-046fffadbbda.png)





References:
1) Huang, Y., Datta, A., Bikson, M., & Parra, L. C. (2019). Realistic volumetric-approach to simulate transcranial electric stimulation—ROAST—a fully automated open-source pipeline. Journal of Neural Engineering, 16(5), 056006. https://doi.org/10.1088/1741-2552/ab208d
2) Indahlastari, A., Albizu, A., Kraft, J. N., O’Shea, A., Nissim, N. R., Dunn, A. L., Carballo, D., Gordon, M. P., Taank, S., Kahn, A. T., Hernandez, C., Zucker, W. M., & Woods, A. J. (2021). Individualized tDCS modeling predicts functional connectivity changes within the working memory network in older adults. Brain Stimulation, 14(5), 1205–1215. https://doi.org/10.1016/j.brs.2021.08.003
3) Albizu, A., Fang, R., Indahlastari, A., O’Shea, A., Stolte, S. E., See, K. B., Boutzoukas, E. M., Kraft, J. N., Nissim, N. R., & Woods, A. J. (2020). Machine learning and individual variability in electric field characteristics predict tDCS treatment response. Brain Stimulation, 13(6), 1753–1764. https://doi.org/10.1016/j.brs.2020.10.001

