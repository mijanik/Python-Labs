import numpy as np

def main():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    print("Numpy: " + str(np.dot(a, b)))
    print(sum([i*j for (i, j) in zip(a, b)]))

if __name__ == "__main__":
    main()