import numpy as np
import random

def main():
    matrix_size = random.randint(1,100)
    A = np.random.rand(matrix_size, matrix_size)
    print(np.linalg.det(A))

if __name__ == "__main__":
    main()