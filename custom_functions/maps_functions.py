"""
Author: Davide Aloi - PhD student - University of Birmingham

"""
import numpy as np


def current_density_efield(e_field: np.ndarray, mask: np.ndarray, conductivities: list):
    """Computing current density (J) from electric field magnitude map and tissue
    conductivities (s) of each voxel in accordance with Ohm’s law: J = sE.
    Default conductivity values (S/m) could be:
    White matter = 0.126 (S/m)
    Grey matter = 0.276 (S/m)
    Cerebrospinal fluid = 1.65 (S/m)

    E_field = numpy array containing the electric field magnitude values at each voxel.

    mask = mask containing only integers (i.e. 1 = white matter, 2 = grey matter, 3 =
    cerebrospinal fluid etc).

    conductivities: list containing the conductivities for each tissue included in the
    mask (1: 0.126, 2: 0.276 etc)."""
    
    if e_field.shape != mask.shape:
        raise Exception("Electric field map and mask should have the same dimension.")
        
    current_density = np.zeros(e_field.shape)
    
    tissue = 1
    for conductivity in conductivities:
        tissue_mask = np.where(mask == tissue, e_field, 0)
        current_density += tissue_mask * conductivity
        tissue += 1
        
    return current_density
