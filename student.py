class Student:
    idNum = ""
    name = ""
    college = ""
    course = ""
    maxUnits = 0
    courses = []
    subjects = []
    sched = []

    def __init__(self, idNum, name, college, course, maxUnits):
        self.idNum = idNum
        self.name = name
        self.college = college
        self.course = course
        self.maxUnits = maxUnits

    def enrollCourse(self, course):
        if self.maxUnits != 0 and self.maxUnits - course.units >= 0 and course.subject not in self.subjects and course.cap != 0 and course.sched not in self.sched:
            print("Enlisted in course " + course.num + " " + course.section + " " + course.subject + " " + course.sched)
            self.courses.append(course)
            self.subjects.append(course.subject)
            self.sched.append(course.sched)
            self.maxUnits -= course.units
            course.students.append(self)
            course.cap -= 1

        elif self.maxUnits == 0:
            print("Cannot enlist course. You have reached your unit cap for the term.")

        elif self.maxUnits - course.units < 0:
            print("Cannot enlist course. You will exceed your unit cap for the term.")

        elif course.subject in self.subjects:
            print("Cannot enlist course. You have already enlisted in a class with the same subject.")

        elif course.sched in self.sched:
            print("Cannot enlist course. You have already enlisted in a class with the same schedule.")

    def dropCourse(self):
        if len(self.courses) == 0:
            print("No classes to drop.")

        else:
            for i in range(len(self.courses)):
                print(self.courses[i].num + " " + self.courses[i].section + " " + self.courses[i].subject + " " + self.courses[i].sched + " " +
                      str(self.courses[i].cap) + "/" + str(self.courses[i].origCap))

            print("Enter the number of the course you would like to drop.")
            numDel = input()

            courseFound = False
            for i in range(len(self.courses)):
                if numDel == self.courses[i].num:
                    self.subjects.remove(self.courses[i].subject)
                    self.sched.remove(self.courses[i].sched)
                    self.courses.remove(self.courses[i])
                    courseFound = True

            if not courseFound:
                print("The number you entered does not match any enlisted courses.")
