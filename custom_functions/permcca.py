# -*- coding: utf-8 -*-
"""
Python implementation of PermCCA (https://github.com/andersonwinkler/PermCCA),
licensed under GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html) as a 
derivative of the original MATLAB code.
Since the Schur decomposition is non-unique there are numerical differences
betwen the MATLAB code and this implementation.
This is a rough translation so there are likely a few bugs, but it generates
sensible enough outputs from a few tests so... ¯\_(ツ)_/¯ Use at your own risk!
"""

import numpy as np
from scipy import linalg as slinalg
from sklearn.utils.extmath import randomized_svd
from sklearn.utils.validation import check_random_state


def _cca(x, y, r, s):
    """
    Runs CCA on inputs `x` and `y`
    Parameters
    ----------
    x : (N, M) array_like
    y : (N, P) array_like
    r : int
    s : int
    Returns
    -------
    a : numpy.ndarray
        Left canonical coefficients
    b : numpy.ndarray
        Right canonical coefficients
    cc : numpy.ndarray
        Canonical correlations
    """

    x, y = np.asarray(x), np.asarray(y)
    n = len(x)

    qx, rx = slinalg.qr(x, mode='economic')
    qy, ry = slinalg.qr(y, mode='economic')

    # this is gonna be more time consuming than just taking the min dimension
    # K = min(np.linalg.matrix_rank(x), np.linalg.matrix_rank(y))
    K = min(min(x.shape), min(y.shape))

    # randomized SVD is very fast for small values of K
    l, d, m = randomized_svd(qx.T @ qy, n_components=K)
    m = m.T
    cc = np.clip(d, 0, 1)

    a = slinalg.lstsq(rx, l * np.sqrt(n - r))[0]
    b = slinalg.lstsq(ry, m * np.sqrt(n - s))[0]

    return a, b, cc


def _center(x):
    """
    Centers (de-means) columns of `x`, dropping constant columns
    Parameters
    ----------
    x : (N, M) array_like
        Input data to be centered
    Returns
    -------
    xdm : (N, P) numpy.ndarray
        Centered input data with constant columns removed
    """

    x = np.asarray(x)
    icte = np.sum(np.diff(x, axis=0), axis=0) != 0
    x = x - x.mean(axis=0)
    return x[:, icte]


def _semiortho(r, sel=None):
    """
    Computes semi-orthogonal matrix according to Huh-Jhun or Theil method
    Parameters
    ----------
    r : (N, Q) array_like
        Matrix to be decomposed
    sel : array_like, optional
    Returns
    -------
    q : (N, S) numpy.ndarray
        Semi-orthogonal version of input matrix
    """

    r = np.asarray(r)
    if sel is None:
        l, q = slinalg.schur(r)
        o = np.abs(np.diag(l)) >= len(r) * np.spacing(l[-1, -1])
        q = q[:, o]
    else:
        sel = np.asarray(sel)
        q = r @ sel @ slinalg.sqrtm(np.inv(sel.T @ r @ sel))
    return q


def permcca(y, x, n_perm=1000, z=None, w=None, sel=None, partial=True,
            seed=None):
    """
    Permutation inference for canonical correlaton analysis (CCA)
    Parameters
    ----------
    y : (N, P) array_like
        Left set of variables. Must have same number of rows as `x`
    x : (N, M) array_like
        Right set of variables. Must have same number of rows as `y`
    n_perm : int, optional
        Number of permutations to run. Default: 1000
    z : (N, Z) array_like, optional
        Nuisance variables for both (partial CCA) or left side (part CCA).
        See `partial` for more information. Default: None
    w : (N, W) array_like, optional
        Nuisance variables for the right side (bipartial CCA). See `partial`
        for more information. Default: None
    sel : array_like, optional
        Selection matrix for nuisance variables. Default: None
    partial : bool, optional
        Whether to run partial CCA instead of part CCA. Default: True
    seed : {None, int, numpy.random.RandomState}, optional
        Random seed for reproducibility of permutations. Default: None
    Returns
    -------
    pfwer : numpy.ndarray
        P-values for canonical modes, FWER corrected via closure
    """

    rs = check_random_state(seed)
    x, y = np.asarray(x), np.asarray(y)

    x, y = _center(x), _center(y)
    if z is not None:
        z = _center(z)
    if w is not None:
        w = _center(w)

    ny, p = y.shape
    nx, q = x.shape
    k = min(p, q)
    if ny != nx:
        raise ValueError('X and Y do not have same number of rows.')
    n = ny
    i = np.eye(n)

    if z is not None:
        r = len(z.T)
        rz = i - (z @ slinalg.pinv(z))
        qz = _semiortho(rz, sel=sel)
    else:
        r = 0
        rz = i.copy()
        qz = i.copy()

    y = qz.T @ rz @ y
    pnew = len(y)

    if w is None and partial:
        w = z
    if w is not None:
        s = len(w.T)
        if partial:
            rw = rz
            qw = qz
        else:
            rw = i @ (w @ slinalg.pinv(w))
            qw = _semiortho(rw, sel)
    else:
        s = 0
        rw = i
        qw = i

    x = qw.T @ rw @ x
    qnew = len(x)

    a, b, *rest = _cca(y, x, r, s)
    u = y @ np.column_stack([a, slinalg.null_space(a.T)])
    v = x @ np.column_stack([b, slinalg.null_space(b.T)])

    cnt = np.zeros(k)
    lw = np.zeros(k)
    from tqdm import tqdm
    for p in range(n_perm):
        if p == 0:
            idxy = range(pnew)
            idxx = range(qnew)
        else:
            idxy = rs.permutation(pnew)
            idxx = rs.permutation(qnew)
    
        for c in range(k):
            *rest, cc = _cca(qz @ u[idxy, c:], qw @ v[idxx, c:], r, s)
            lwtmp = -np.cumsum(np.log(1 - (cc ** 2)))[::-1]
            lw[c] = lwtmp[0]

        if p == 0:
            lw1 = lw.copy()

        cnt = cnt + (lw >= lw1)

    punc = cnt / (n_perm + 1)
    pfwer = np.maximum.accumulate(punc)

    return pfwer