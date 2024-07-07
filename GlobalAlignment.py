# IQB ASSIGNMENT 1
# Q1 - Global Alignment

import numpy as np
import pandas as pd


def nw(x, y, match=2, mismatch=-3, gap=-1):
    nx = len(x)
    ny = len(y)

    # Initialization of the matrix.
    F = np.zeros((nx + 1, ny + 1))
    #! SINCE THE GAP PENALTY IS ALREADY NEGATIVE THERE SHOULD BE NO NEGATIVE SIGN
    F[:, 0] = np.linspace(0, gap * nx, nx + 1)
    F[0, :] = np.linspace(0, gap * ny, ny + 1)

    #? bug resolved the P matrix should be initialised before the filling of matrrix so that
    #? it can be used to store the tracing of the filling and help in traceback
    P = np.zeros((nx + 1, ny + 1), dtype=int)
    P[:, 0] = 3
    P[0, :] = 4

    # Arrays for calculating score for three directions: diagonal, down, right
    arr = np.zeros(3)

    #? another bug found is index out of bounds the nested for loops should run from 0 to n-1 not from 1 to n so they have been corrected
    for i in range(nx):
        for j in range(ny):
            if x[i] == y[j]:
                arr[0] = F[i, j] + match       #! incase of match
            else:
                arr[0] = F[i, j] + mismatch     #! incase of mismatch PENALTY WHICH IS ALREADY NEGATIVE

            arr[1] = F[i, j + 1] + gap    #!gap(NEGATIVE IN VALUE)
            arr[2] = F[i + 1, j] + gap    #!gap(NEGATIVE IN VALUE)
            a_final = np.max(arr)         # FINDING THE MAX OF ALL THREE VALUES
            F[i + 1, j + 1] = a_final
            #! this is done so that we can traceback the alignment
            if arr[0] == a_final:
                P[i + 1, j + 1] += 2  # match/mismatch
            if arr[1] == a_final:
                P[i + 1, j + 1] += 3  # vertical move
            if arr[2] == a_final:
                P[i + 1, j + 1] += 4  # horizontal move

    # Print scoring matrix using pandas DataFrame
    print("Scoring Matrix:")
    #! corrected the ordering of the process the first sequence is on the top and second sequence on the left
    df = pd.DataFrame(F, index=['-'] + list(x), columns=['-'] + list(y)).transpose()
    print(df)

    # Trace through optimal alignments and their scores.
    alignments = []

    def traceback(i, j, rx, ry, score):
        if i == 0 and j == 0:
            alignments.append((rx[::-1], ry[::-1], score))
            return
        if P[i, j] in [2, 5, 6, 9]:
            traceback(i - 1, j - 1, rx + x[i - 1], ry + y[j - 1], score + (match if x[i - 1] == y[j - 1] else mismatch))
        if P[i, j] in [3, 5, 7, 9]:
            traceback(i - 1, j, rx + x[i - 1], ry + '-', score + gap)
        if P[i, j] in [4, 6, 7, 9]:
            traceback(i, j - 1, rx + '-', ry + y[j - 1], score + gap)

    traceback(nx, ny, '', '', 0)


    # Find the best score
    best_score = max(alignments, key=lambda x: x[2])[2]

    # Print all alignments with the best score
    print("\nAll Optimal Alignments:")
    for align in alignments:
        print(f"Alignment:\n{align[0]}\n{align[1]}\nScore: {align[2]}\n")

    # Print the optimal alignment(s) with the highest score
    print("Best alignments which are the Optimal Alignment(s) with Highest Score:")
    for align in alignments:
        if align[2] == best_score:
            print(f"Alignment:\n{align[0]}\n{align[1]}\nScore: {align[2]}\n")
    #print

seq1 = "GATGCGCAG"
seq2 = "GGCAGTA"

nw(seq1, seq2)

