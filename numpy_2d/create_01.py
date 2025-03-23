import numpy as np

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = np.array(a)

print(A.ndim)  # 2

b = [A+10, A+20, A+30]
B = np.array(b)
print(B.ndim)
print(B)