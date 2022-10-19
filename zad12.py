import numpy as np


def main():
    A = np.random.rand(128, 128)
    B = np.random.rand(128, 128)
    C = np.add(A, B)
    print(C)

if __name__ == "__main__":
    main()