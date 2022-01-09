Aloi Davide - PhD Student (UoB)

Analysis of electric field magnitudes (wp2a dataset only at the moment) and correlation analysis with Dynamic Causal Modelling (DCM) results. 

The goal of these analyses is to establish whether there is a relationship between single-subject electric field (E-field) magnitudes generated with the [ROAST](https://github.com/andypotatohy/roast#5-outputs-of-roast-software) pipeline (Huang et al., 2019) and changes in effective connectivity within the motor network, derived using DCM and parametric empirical bayes (PEB). 

The two analyses are:
1) Correlation analysis between E-field magnitude - medians and max values - (or the current density?) in the motor cortex (M1) and Thalamus (Th) with self- / between-connectivities (M1 and Th only?) as derived from the DCM. e.g. Indahlastari et al. (2021). At the moment I am correlating e-field measures only with DCM measures derived from the contrast pre vs post Day-1 anodal only. However, I should also correlate those e-field measures with DCM measures derived from the contrast pre vs post Day-1 sham. I expect to find correlations between e-field measures and DCM measures for the anodal condition but not for sham. 
2) Pattern-recognition analysis using support vector machine (SVM) learning algorithm on MRI-derived tDCS current models to provide classification of tDCS treatment response (as reflected by increased M1-TH or TH-M1 connectivity or whatever other measure we decide). e.g. Albizu et al. (2020). The question here is: can we classify people who had an increase in thalamo-cortical connectivity  using features from the MRI-current models? 

Those two analyses require similar preprocessing steps. Here's the list of the steps I've done and the respective scripts.
WP2A: I start from a dataset containing 22 folders (one per participant), each containing a T1 and a T2 scan (except for subject 16 who has only a T1). 

1) Renaming of anatomical scans (wp2a_roast_1_rename_scans.py): this renames the anatomical scans of each participant (i.e. sub-01_T1.nii etc). 
2) ROAST simulations (wp2a_roast_2_roast_simulation.m): this script runs the ROAST simulations. ROAST 














References:
1) Huang, Y., Datta, A., Bikson, M., & Parra, L. C. (2019). Realistic volumetric-approach to simulate transcranial electric stimulation—ROAST—a fully automated open-source pipeline. Journal of Neural Engineering, 16(5), 056006. https://doi.org/10.1088/1741-2552/ab208d
2) Indahlastari, A., Albizu, A., Kraft, J. N., O’Shea, A., Nissim, N. R., Dunn, A. L., Carballo, D., Gordon, M. P., Taank, S., Kahn, A. T., Hernandez, C., Zucker, W. M., & Woods, A. J. (2021). Individualized tDCS modeling predicts functional connectivity changes within the working memory network in older adults. Brain Stimulation, 14(5), 1205–1215. https://doi.org/10.1016/j.brs.2021.08.003
3) Albizu, A., Fang, R., Indahlastari, A., O’Shea, A., Stolte, S. E., See, K. B., Boutzoukas, E. M., Kraft, J. N., Nissim, N. R., & Woods, A. J. (2020). Machine learning and individual variability in electric field characteristics predict tDCS treatment response. Brain Stimulation, 13(6), 1753–1764. https://doi.org/10.1016/j.brs.2020.10.001

