from student import *
from course import *

courses = []

courses.append(Course("0001", "CSADPRG", "S11", "Ms. Charibeth Cheng", "MW 915-1045", 3, 45))
courses.append(Course("0002", "CSADPRG", "S13", "Ms. Kedren Villena", "TH 915-1045", 3, 45))
courses.append(Course("0003", "CSADPRG", "S15", "Mr. Kedren Villena", "TH 1100-1230", 3, 45))

courses.append(Course("0004", "CCINFOM", "S12", "Ms. Estefanie Bertumen", "TH 1430-1600", 3, 45))
courses.append(Course("0005", "CCINFOM", "S14", "Mr. Oliver Malabanan", "TH 1100-1230", 3, 45))
courses.append(Course("0006", "CCINFOM", "S16", "Mr. Oliver Malabanan", "TH 1245-1415", 3, 45))

courses.append(Course("0007", "CSALGCM", "S17", "Mr. Neil Gallego", "MW 1430-1600", 3, 45))
courses.append(Course("0008", "CSALGCM", "S11", "Mr. Austin Fernandez", "MW 1100-1230", 3, 45))
courses.append(Course("0009", "CSALGCM", "S13", "Mr. Austin Fernandez", "TH 1100-1230", 3, 45))

courses.append(Course("0010", "CSINTSY", "S18", "Ms. Joanna Rivera", "MW 915-1045", 3, 45))
courses.append(Course("0011", "CSINTSY", "S12", "Ms. Joanna Rivera", "MW 1100-1230", 3, 45))
courses.append(Course("0012", "CSINTSY", "S14", "Ms. Joanna Rivera", "TH 915-1045", 3, 45))

courses.append(Course("0013", "GEDANCE", "S15", "Ms. Margarita Tapang", "F 730-930", 2, 45))
courses.append(Course("0014", "GEDANCE", "S17", "Mr. Efren Bacani", "F 730-930", 2, 45))
courses.append(Course("0015", "GEDANCE", "S11", "Ms. Joy Samson", "F 730-930", 2, 45))

students = []
students.append(Student("11828870", "Gabriel Minamedez", "CCS", "BS CS-ST", 21))
students.append(Student("11812345", "Juan Dela Cruz", "CCS", "BS IT", 21))

print("Good day, Lasallian Achiever!")
print("What would you like to do?")
print("[1] Enlist a Class\n[2] Drop a Class\n[3] View My Classes\n[4] View Offered Classes\n[5] Exit")
choice = input()

while choice != "5":
    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid input!")
        while choice not in ("1", "2", "3", "4", "5"):
            print("What would you like to do?")
            print("[1] Enlist a Class\n[2] Drop a Class\n[3] View My Classes\n[4] View Offered Classes\n[5] Exit")
            choice = input()

    elif choice == "1":
        for i in range(len(courses)):
            print(str(i) + " " + courses[i].num + " " + courses[i].section + " " + courses[i].subject + " " + courses[i].sched + " " +
            str(courses[i].cap) + "/" + str(courses[i].origCap))
        print("Enter the index of the course you would like to enlist: ")
        courseChoice = int(input())
        students[0].enrollCourse(courses[courseChoice])
        print("What would you like to do?")
        print("[1] Enlist a Class\n[2] Drop a Class\n[3] View My Classes\n[4] View Offered Classes\n[5] Exit")
        choice = input()

    elif choice == "2":
        students[0].dropCourse()
        print("What would you like to do?")
        print("[1] Enlist a Class\n[2] Drop a Class\n[3] View My Classes\n[4] View Offered Classes\n[5] Exit")
        choice = input()

    elif choice == "3":
        if len(students[0].courses) == 0:
            print("You have not enlisted in any courses yet.")
            print("What would you like to do?")
            print("[1] Enlist a Class\n[2] Drop a Class\n[3] View My Classes\n[4] View Offered Classes\n[5] Exit")
            choice = input()

        else:
            for i in range(len(students[0].courses)):
                print(print(students[0].courses[i].num + " " + students[0].courses[i].section + " " + students[0].courses[i].subject + " " +
                            students[0].courses[i].sched + " " + str(students[0].courses[i].cap) + "/" + str(students[0].courses[i].origCap)))
            print("What would you like to do?")
            print("[1] Enlist a Class\n[2] Drop a Class\n[3] View My Classes\n[4] View Offered Classes\n[5] Exit")
            choice = input()

    elif choice == "4":
        for i in range(len(courses)):
            print(str(i) + " " + courses[i].num + " " + courses[i].section + " " + courses[i].subject + " " + courses[i].sched + " " +
                  str(courses[i].cap) + "/" + str(courses[i].origCap))
        print("What would you like to do?")
        print("[1] Enlist a Class\n[2] Drop a Class\n[3] View My Classes\n[4] View Offered Classes\n[5] Exit")
        choice = input()

    elif choice == "5":
        print("Thank you for using the facility. Have a good day, Lasallian!")
