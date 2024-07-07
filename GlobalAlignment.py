# IQB ASSIGNMENT 1
# Q1 - Global Alignment

import numpy as np
import pandas as pd

def nw(x, y, match=2, mismatch=-3, gap=-1):
    nx = len(x)
    ny = len(y)
    
    # Initialization of the matrix.
    F = np.zeros((nx + 1, ny + 1))
    F[:, 0] = np.linspace(0, -gap * nx, nx + 1)
    F[0, :] = np.linspace(0, -gap * ny, ny + 1)

    # Pointers to trace through an optimal alignment.
    # Matrix filling.
    for i in range(1, nx + 1):
        for j in range(1, ny + 1):
            #complete the code

    P = np.zeros((nx + 1, ny + 1), dtype=int)
    P[:, 0] = 3
    P[0, :] = 4


    # Print scoring matrix using pandas DataFrame
    print("Scoring Matrix:")
    df = pd.DataFrame(F, index=['-'] + list(x), columns=['-'] + list(y))
    print(df)

    # Trace through an optimal alignment.
    i = nx
    j = ny
    rx = []
    ry = []
    while i > 0 or j > 0:
        if P[i, j] in [2, 5, 6, 9]:
            #complete the code
        elif P[i, j] in [3, 5, 7, 9]:
            #complete the code
        elif P[i, j] in [4, 6, 7, 9]:
            #complete the code

    # Reverse the strings.
    rx = ''.join(rx)[::-1]
    ry = ''.join(ry)[::-1]

    return '\n'.join([rx, ry])

seq1 = "GATGCGCAG"
seq2 = "GGCAGTA" 

print(nw(seq1, seq2))
