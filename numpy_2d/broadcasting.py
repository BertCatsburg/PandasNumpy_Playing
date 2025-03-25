import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9, 10])

print(A*B)  # [ 4 10 18]
print((A * B).sum())

try:
    print(A*C)
except Exception as e:
    print(e)  # operands could not be broadcast together with shapes (3,) (4,)
