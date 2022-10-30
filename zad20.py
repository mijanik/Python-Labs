import threading

Forks = [1, 1, 1, 1, 1]

class Philosophers:
    def __init__(self, seat: str):
        self.seat = seat
        self.state = "Thinking"
        match seat:
            case "A":
                available_forks = ["5", "1"]
            case "B":
                available_forks = ["1", "2"]
            case "C":
                available_forks = ["2", "3"]
            case "D":
                available_forks = ["3", "4"]
            case "E":
                available_forks = ["4", "5"]


def philosopher_brain(phil_state: dict):
    pass


def main():
    sokrates = Philosophers()

    pass


if __name__ == '__main__':

    main()
