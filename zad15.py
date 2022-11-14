class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def print(self):
        print(str(self.real) + " + " + str(self.imag) + "i")

def main():
    #test example:
    x = Complex(1, 1)
    y = Complex(-5, 4)
    z = x + y
    t = x - y

    z.print()
    t.print()

if __name__ == "__main__":
    main()