
import numpy as np

P = np.array([[1, 0], [0, 1]])
C = np.array([[3, 2], [5, 7]])

det = int(round(np.linalg.det(P))) % 26
inv_det = pow(det, -1, 26)

adj = np.array([[P[1,1], -P[0,1]],
                [-P[1,0], P[0,0]]])

P_inv = (inv_det * adj) % 26
K = (C @ P_inv) % 26

print("Recovered Key:")
print(K)
