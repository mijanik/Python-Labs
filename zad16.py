class Calculator:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.result = 0.0

    def read(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        self.result =  self.a + self.b

    def sub(self):
        self.result = self.a - self.b

    def mul(self):
        self.result = self.a * self.b

    def div(self):
        self.result = self.a / self.b

    def interface(self):
        print("Hello!")
        choice = 1
        while choice != "0":
            choice = input("Enter: 0 - exit\n1 - Calculate!\n")
            if choice == "0":
                return
            a, sign, b = input("Enter equation example: 1 + 1\n").split()
            a = float(a)
            b = float(b)
            self.read(a, b)
            match sign:
                case "+":
                    self.sum()
                case "-":
                    self.sub()
                case "*":
                    self.mul()
                case "/":
                    self.div()
            print("Result = " + str(self.result))

        return


def main():
    myCalculator = Calculator()
    myCalculator.interface()
    pass


if __name__ == "__main__":
    main()