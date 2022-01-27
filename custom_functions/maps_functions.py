"""
Author: Davide Aloi - PhD student - University of Birmingham - Centre for Human Brain Health
"""
import numpy as np


def current_density_efield(e_field: np.ndarray, mask: np.ndarray, conductivities: list):
    """Computing current density (J) from electric field magnitude map and tissue
    conductivities (s) of each voxel in accordance with Ohm’s law: J = sE.
    Default conductivity values (S/m) could be:
    White matter = 0.126 (S/m)
    Grey matter = 0.276 (S/m)
    Cerebrospinal fluid = 1.65 (S/m)

    Args:
    -------
    e_field: numpy array
        array with electric field magnitude values.

    mask: numpy array
        array of integers (i.e. 1 = white matter, 2 = grey matter, 3 = cerebrospinal
        fluid etc).

    conductivities: list
        list of conductivities for each tissue included in the mask (0: 0.126, 1: 0.276, 
        2: 1.65)
        

    Returns:
    -------
    numpy array with the same shape of e_field and with current density values"""
    
    
    if e_field.shape != mask.shape:
        raise Exception("Electric field map and mask should have the same dimension.")
        
    current_density = np.zeros(e_field.shape)
    
    tissue = 1 # ignoring tissue = 0
    for conductivity in conductivities:
        tissue_mask = np.where(mask == tissue, e_field, 0)
        current_density += tissue_mask * conductivity
        tissue += 1
        
    return current_density
