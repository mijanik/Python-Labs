def main():
    name, surname, birthdate = input("Podaj imie nazwisko i rok urodzenia: \n").split(" ")
    print(f"Imię: {name}\nNazwisko: {surname}\nData urodzenia: {birthdate}")

if __name__ == "__main__":
    main()