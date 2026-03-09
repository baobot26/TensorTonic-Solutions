import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    pass
    A_org = np.asarray(A, dtype=float)
    A_T = np.zeros((A_org.shape[1], A_org.shape[0]))
    for i in range(A_org.shape[0]):
        for j in range(A_org.shape[1]):
            A_T[j][i] = A_org[i][j]
    return A_T