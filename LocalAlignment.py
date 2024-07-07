import numpy as np
import pandas as pd

def local_alignment(x, y, match=2, mismatch=-1, gap=-3):
    nx = len(x)
    ny = len(y)
    
    # Initialization of the matrix.
    F = np.zeros((nx + 1, ny + 1))
    
    # Initialize traceback matrix
    P = np.zeros((nx + 1, ny + 1), dtype=int)
    
    # Arrays for calculating score for three directions: diagonal, down, right
    arr = np.zeros(3)

    for i in range(1, nx + 1):
        for j in range(1, ny + 1):
            if x[i - 1] == y[j - 1]:
                arr[0] = F[i - 1, j - 1] + match
            else:
                arr[0] = F[i - 1, j - 1] + mismatch
            arr[1] = F[i - 1, j] + gap
            arr[2] = F[i, j - 1] + gap

            # If negative values are coming, set arr[0] to 0 as in Local alignment minimum value is 0
            arr[0] = max(arr[0], 0)
            
            a_final = np.max(arr)
            F[i, j] = a_final
            
            # Traceback matrix
            if a_final == 0:
                P[i, j] = 0
            else:
                if arr[0] == a_final:
                    P[i, j] += 2  # match/mismatch
                if arr[1] == a_final:
                    P[i, j] += 3  # vertical move
                if arr[2] == a_final:
                    P[i, j] += 4  # horizontal move

    # Print scoring matrix using pandas DataFrame
    print("Scoring Matrix:")
    df = pd.DataFrame(F, index=['-'] + list(x), columns=['-'] + list(y)).transpose()
    print(df)

    # Find maximum value and its indices in matrix F
    max_value = np.max(F)
    max_indices = np.argwhere(F == max_value)

    # Traceback through optimal alignment paths starting from maximum value indices
    alignments = []
    for idx in max_indices:
        traceback(idx[0], idx[1], '', '', 0, F, P, x, y, alignments)

    # Print all optimal alignments
    print("\nAll Optimal Alignments:")
    for align in alignments:
        print(f"Alignment:\n{align[0]}\n{align[1]}\nScore: {align[2]}\n")

    # Print the optimal alignment(s) with the highest score
    print("Best alignment which are Optimal Alignment(s) with Highest Score:")
    best_score = max(alignments, key=lambda x: x[2])[2]
    for align in alignments:
        if align[2] == best_score:
            print(f"Alignment:\n{align[0]}\n{align[1]}\nScore: {align[2]}\n")


def traceback(i, j, rx, ry, score, F, P, x, y, alignments):
    if F[i, j] == 0:
        alignments.append((rx[::-1], ry[::-1], score))
        return
    
    if P[i, j] in [2, 5, 6, 9]:
        traceback(i - 1, j - 1, rx + x[i - 1], ry + y[j - 1], score + (2 if x[i - 1] == y[j - 1] else -1), F, P, x, y, alignments)
    if P[i, j] in [3, 5, 7, 9]:
        traceback(i - 1, j, rx + x[i - 1], ry + '-', score - 3, F, P, x, y, alignments)
    if P[i, j] in [4, 6, 7, 9]:
        traceback(i, j - 1, rx + '-', ry + y[j - 1], score - 3, F, P, x, y, alignments)


seq1 = "GATGCGCAG"
seq2 = "GGCAGTA"

local_alignment(seq1, seq2)
