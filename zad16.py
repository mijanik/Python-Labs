from zad15 import Complex


class Calculator:
    def __init__(self):
        self.a = Complex(0, 0)
        self.b = Complex(0, 0)
        self.result = Complex(0, 0)

    def read(self, a_real, a_imag, b_real, b_imag):
        self.a.real = a_real
        self.a.imag = a_imag
        self.b.real = b_real
        self.b.imag = b_imag

    def sum(self):
        self.result = self.a + self.b

    def sub(self):
        self.result = self.a - self.b

    def interface(self):
        print("Hello!")
        choice = 1
        while choice != "0":
            choice = input("Enter: 0 to exit\nEnter anything else to start!")
            if choice == "0":
                return
            a_real, a_imag, sign, b_real, b_imag = input("Enter equation, example: -1 +2i - 2 -2i\n").split(" ")
            self.read(float(a_real), float(a_imag[:-1]), float(b_real), float(b_imag[:-1]))
            match sign:
                case "+":
                    self.sum()
                case "-":
                    self.sub()
                case other:
                    print("Invalid operation!")

            print("Result = ")
            self.result.print()

        return


def main():
    myCalculator = Calculator()
    myCalculator.interface()
    pass


if __name__ == "__main__":
    main()