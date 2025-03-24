import numpy as np


def add_five(x):
    return x + 5


if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5])
    av = np.vectorize(add_five)  # Ready the function for processing on numpy arrays

    new_a = av(a)
    print(new_a)  # [ 6  7  8  9 10]
