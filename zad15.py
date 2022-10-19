class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

def main():
    x = Complex(1, 1)
    y = Complex(-5, 4)
    z = x + y
    t = x - y
    print(str(z.real) + " + " + str(z.imag) + ("j\n"))
    print(str(t.real) + " + " + str(t.imag) + ("j\n"))


if __name__ == "__main__":
    main()