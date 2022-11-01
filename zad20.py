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


def philosopher_brain(philosopher: Philosophers):
    while finished == 0:
        if Forks[philosopher.available_forks[0]] == 1 or philosopher.used_forks[0] == 1:
            #if available or posessed by this philospher

            if philosopher.used_forks[0] == 0:
                philosopher.take_fork(0) #take if not taken

            if Forks[philosopher.available_forks[1]] == 1 or philosopher.used_forks[1] == 1:
                if philosopher.used_forks[1] == 0:
                    philosopher.take_fork(1)  # take if not taken
                    philosopher.state = "Eating"
                    print(str(philosopher.seat) + " started to eat")

                    time.sleep(random.randint(5, 10))
                    philosopher.return_fork(0)
                    philosopher.return_fork(1)

        else:
            if philosopher.state != "Thinking":
                philosopher.state = "Thinking"
                print(str(philosopher.seat) + " started to think")
                time.sleep(random.randint(5, 10))


    return



def main():
    sokrates = Philosophers("A")
    platon = Philosophers("B")
    archimedes = Philosophers("C")
    pitagoras = Philosophers("D")
    kant = Philosophers("E")
    threading.Thread(target=philosopher_brain, args=(sokrates, )).start()
    threading.Thread(target=philosopher_brain, args=(platon, )).start()
    threading.Thread(target=philosopher_brain, args=(archimedes,)).start()
    threading.Thread(target=philosopher_brain, args=(pitagoras,)).start()
    threading.Thread(target=philosopher_brain, args=(kant,)).start()
    #threading.Thread(target=philosopher_brain, args=(kant,)).start()

    for i in range(30):
        print(Forks)
        time.sleep(1)
    global finished
    finished = 1
    while threading.active_count() != 1:
        pass
    return

if __name__ == '__main__':
    main()
