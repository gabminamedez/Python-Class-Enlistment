class Course:
    num = ""
    subject = ""
    section = ""
    prof = ""
    sched = ""
    units = 0
    cap = 0
    origCap = 0
    students = []

    def __init__(self, num, subject, section, prof, sched, units, cap):
        self.num = num
        self.subject = subject
        self.section = section
        self.prof = prof
        self.sched = sched
        self.units = units
        self.cap = cap
        self.origCap = cap
