import numpy as np

def nullspace(A, atol=1e-13, rtol=0): #Source: SciPy
    A = np.atleast_2d(A)
    u, s, vh = np.linalg.svd(A)
    tol = max(atol, rtol * s[0])
    nnz = (s >= tol).sum()
    ns = vh[nnz:].conj().T
    return ns

def lahenda(km):
    vastus = []
    try:
        ns = nullspace(np.array(km).T)
        min = abs(ns[0][0])
        for i in range(1, len(ns)):
            if abs(ns[i][0]) < min:
                min = abs(ns[i][0])
        if min > 1/100000000:
            for i in range(len(ns)):
                vastus.append(int(round(ns[i][0]/min)))         
    except:
        pass
    return vastus
