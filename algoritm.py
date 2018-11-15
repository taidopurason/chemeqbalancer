import numpy as np

def nullspace(A, atol=1e-15, rtol=0): #Source: SciPy
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
        print(ns)
        min = abs(ns[0][0])
        for i in range(1, len(ns)):
            if abs(ns[i][0]) < min:
                min = abs(ns[i][0])
        print(min)
        if min > 1/100000000:
            for i in range(len(ns)):
                vastus.append(round(ns[i][0]/min, 1))
        k = 0
        isint = 0
        while not isint:
            isint = 1
            k += 1
            for i in vastus:
                if abs(k*i - round(k*i, 0)) > 1/1000000:
                    isint = 0
                    break
            
    except:
        pass
    return [int(k*i) for i in vastus]
