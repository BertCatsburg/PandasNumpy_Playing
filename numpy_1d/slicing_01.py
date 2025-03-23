import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
b = a[3:7]
print(b)  # [3 4 5 6]

b = a[-1:-3:-1]
print(b)  # [12, 11]

a[1:3] = [100, 101]
print(a[0:5])  # [  0 100 101   3   4]