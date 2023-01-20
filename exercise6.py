import numpy as np

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

#np.allclose() function is used to find if two arrays are element-wise equal within a tolerance value (usually a small positive number).

print(np.allclose(A, B))
