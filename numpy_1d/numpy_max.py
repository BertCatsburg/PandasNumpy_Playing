import numpy as np
import random

a = np.array([random.randint(0, 2500) for _ in range(20)])
print(a.max())
