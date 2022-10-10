def main():
    name, surname, birthdate = input("Podaj imie nazwisko i rok urodzenia: \n").split(" ")
    print(name + "\n" + surname + "\n" + birthdate)

if __name__ == "__main__":
    main()