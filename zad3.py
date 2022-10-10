def main():
    pin = "0000"
    while True:
        if pin == "0000":
            pin = input("Podaj nowy PIN:\n")

        input_pin = input("Podaj PIN aby poznac tajna wiadomosc:\n")
        if input_pin == pin:
            print("Tajna wiadomosc\n")
        else:
            print("Błędny PIN!")


if __name__ == "__main__":
    main()