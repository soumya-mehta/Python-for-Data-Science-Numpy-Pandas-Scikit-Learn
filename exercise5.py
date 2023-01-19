import numpy as np

A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

#np.isnan() function tests the list element-wise whether it is NaN or not and returns the result as a boolean array.

print(np.isnan(A))
