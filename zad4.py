import os

def main():
    path = "dev"
    count = 0
    for file in os.listdir(path):
        count+=1
        print(file)
    print("liczba wszystkich plikow w katalogu: " + str(count))


if __name__ == "__main__":
    main()