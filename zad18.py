import csv


def read_csv():
    with open('example.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(', '.join(row))


def add_csv(title: str, description: str):
    fields = [title, description]
    with open('example.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(fields)


def rem_csv(to_remove: str):
    lines = list()
    with open('example.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == to_remove:
                    lines.remove(row)

    with open('example.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


def main():
    print("Database content:\n")
    read_csv()
    choice = input("Enter: \n1 - write row to CSV\n2 - delete from CSV\n")

    match choice:
        case "1":
            title = input("Type Title:\n")
            description = input("Type Description:\n")
            add_csv(title, description)

        case "2":
            to_remove = input("Type Title or Description of Task to remove:\n")
            rem_csv(to_remove)

        case _:
            print("Invalid operation")


if __name__ == '__main__':
    main()
