import numpy as np


def main():
    A = np.random.rand(8, 8)
    B = np.random.rand(8, 8)
    C = np.matmul(A, B)
    print(C)

if __name__ == "__main__":
    main()