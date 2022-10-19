import csv
def main():
    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    #with open('example.csv', 'w', newline='') as file:
    #    writer = csv.writer(file)
    #    writer.writerow(["Task ID", "Task title", "Task description"])
    #    writer.writerow([1, "Do Homework", "Maths"])
    #    writer.writerow([2, "Make a bubble sort", "its important to make it today"])


if __name__ == '__main__':
    main()