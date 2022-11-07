from xml.dom import minidom
import xml.etree.ElementTree as ET

def read_xml():
    # parse an xml file by name
    mydoc = minidom.parse('example.xml')
    student_list = mydoc.getElementsByTagName('student')
    print('\nAll Students and grades:')
    for elem in student_list:
        print("Name: " + elem.attributes['name'].value)
        print("Grade: " + elem.attributes['grade'].value)

def add_xml(my_name: str, my_grade: str):
    # parse an xml file by name
    mydoc = minidom.parse('example.xml')
    newstudent = mydoc.createElement("student")
    newstudent.setAttribute("name", my_name)
    newstudent.setAttribute("grade", my_grade)
    mydoc.firstChild.appendChild(newstudent)

    with open("example-new.xml", "w") as fs:
        fs.write(mydoc.toxml())
        fs.close()

def main():
    choice = input("Enter: 0 - exit\n1 - print example.xml\n2 - add new student\n")

    match choice:
        case "0":
            pass
        case "1":
            read_xml()
        case "2":
            name, grade = input("Write in format:  First_name Last_name, grade\n").split(", ")
            add_xml(name, grade)

    return


if __name__ == "__main__":
    main()