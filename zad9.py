import math

def calculate_equation(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    x1 = 0.0
    x2 = 0.0
    delta = b*b - 4*a*c
    if delta < 0:
        real_solutions = 0
    elif delta == 0:
        real_solutions = 1
        x1 = (-1*b)/(2*a)
    else:
        real_solutions = 2
        x1 = (-1 * b - math.sqrt(delta)) / (2 * a)
        x2 = (-1 * b + math.sqrt(delta)) / (2 * a)

    return real_solutions, x1, x2

def main():
    a, b, c = input("Enter a, b and c parameters of square equation").split(" ")
    real_solutions, x1, x2,  = calculate_equation(a, b, c)
    if real_solutions == 0:
        print("No real solutions!")
    elif real_solutions == 1:
        print("One real solution: " + str(x1))
    else:
        print("x1 = " + str(x1) + " and x2 = " + str(x2) + "\n")


if __name__ == "__main__":
    main()