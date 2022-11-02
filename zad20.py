import threading
import time
import random

Forks = [1, 1, 1, 1, 1] # 1 if available
finished = 0


class Philosophers:
    def __init__(self, seat: str):
        self.seat = seat
        self.state = "Thinking" #default
        self.used_forks = [0, 0] # 1 if taken

        match seat:
            case "A":
                self.available_forks = [4, 0]
            case "B":
                self.available_forks = [0, 1]
            case "C":
                self.available_forks = [1, 2]
            case "D":
                self.available_forks = [2, 3]
            case "E":
                self.available_forks = [3, 4]

    def take_fork(self, fork_id: int):
        self.used_forks[fork_id] = 1
        Forks[self.available_forks[fork_id]] = 0
        print(str(self.seat) + " took fork " + str(self.available_forks[fork_id]))

    def return_fork(self, fork_id: int):
        self.used_forks[fork_id] = 0
        Forks[self.available_forks[fork_id]] = 1
        print(str(self.seat) + " returned fork " + str(self.available_forks[fork_id]))

class Waiter:
    def __init__(self, A: Philosophers, B: Philosophers, C: Philosophers, D: Philosophers, E: Philosophers):
        self.fork_reservation = ["0", "0", "0", "0", "0"]  # 0 = not reserved, A, B, C, D, E if reserved
        pass

    def ask_fork(self, philosopher: Philosophers, fork_id) -> bool:

        match fork_id:
            case 0:
                pass
            case 1:
                pass

        # if fork is available and not reserved or reserved by himself
        if Forks[philosopher.available_forks[fork_id]] == 1 and (self.fork_reservation[philosopher.available_forks[fork_id]] == "0" or self.fork_reservation[philosopher.available_forks[fork_id]] == philosopher.seat):
            self.fork_reservation[philosopher.available_forks[fork_id]] = "0"
            return True
        else:
            if self.fork_reservation[philosopher.available_forks[fork_id]] == "0":  # if second fork is not reserved yet
                self.fork_reservation[philosopher.available_forks[fork_id]] = philosopher.seat
            if fork_id == 0 and self.fork_reservation[philosopher.available_forks[1]] == "0":
                self.fork_reservation[philosopher.available_forks[1]] = philosopher.seat

            return False




def philosopher_brain(philosopher: Philosophers, waiter: Waiter):
    time.sleep(random.randint(1, 10))
    while finished == 0:
        # if Forks[philosopher.available_forks[0]] == 1 or philosopher.used_forks[0] == 1:
        if waiter.ask_fork(philosopher, 0) or philosopher.used_forks[0] == 1:
            # if available or already posessed by this philospher

            if philosopher.used_forks[0] == 0:
                philosopher.take_fork(0) #take if not taken

            # if Forks[philosopher.available_forks[1]] == 1 or philosopher.used_forks[1] == 1:
            if waiter.ask_fork(philosopher, 1):
                if philosopher.used_forks[1] == 0:
                    philosopher.take_fork(1)  # take if not taken
                    philosopher.state = "Eating"
                    print(str(philosopher.seat) + " started to eat")

                    time.sleep(random.randint(5, 10))
                    philosopher.return_fork(0)
                    philosopher.return_fork(1)

                    philosopher.state = "Thinking"
                    print(str(philosopher.seat) + " started to think")
                    time.sleep(random.randint(10, 20))


        else:
            print(str(philosopher.seat) + " tried to start eating but was unable")
            time.sleep(random.randint(1, 3))


    return



def supervisor(a: Philosophers, b: Philosophers, c: Philosophers, d: Philosophers, e: Philosophers, waiter: Waiter):
    while finished == 0:
        print("Availability of Forks: " + str(Forks))
        print("Fork reservation list: " + str(waiter.fork_reservation))
        print("A: " + a.state + ", B: " + b.state + ", C: " + c.state + ", D: " + d.state + ", E: " + e.state)
        if all(item == 0 for item in Forks) and a.state == "Thinking" and b.state == "Thinking" and c.state == "Thinking" and d.state == "Thinking" and e.state == "Thinking":
            print("DEADLOCK!")
        time.sleep(1)
    return


def main():
    sokrates = Philosophers("A")
    platon = Philosophers("B")
    archimedes = Philosophers("C")
    pitagoras = Philosophers("D")
    kant = Philosophers("E")
    waiter = Waiter(sokrates, platon, archimedes, pitagoras, kant)
    threading.Thread(target=philosopher_brain, args=(sokrates, waiter)).start()
    threading.Thread(target=philosopher_brain, args=(platon, waiter)).start()
    threading.Thread(target=philosopher_brain, args=(archimedes, waiter)).start()
    threading.Thread(target=philosopher_brain, args=(pitagoras, waiter)).start()
    threading.Thread(target=philosopher_brain, args=(kant, waiter)).start()
    threading.Thread(target=supervisor, args=(sokrates, platon, archimedes, pitagoras, kant, waiter)).start()

    time.sleep(30)
    global finished
    finished = 1
    while threading.active_count() != 1:
        pass
    return

if __name__ == '__main__':
    main()
