class student:
    def __init__(self, name, subject_1, subject_2, subject_3):
        self.name = name
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        self.subject_3 = subject_3

    def average(self):
        avg = ((self.subject_1 + self.subject_2 + self.subject_3)) / 3
        print(f"your name is {name} and your average marks is {avg}")


name = input("enter your name = ")
subject1 = int(input("enter your marks = "))
subject2 = int(input("enter your marks = "))
subject3 = int(input("enter your marks = "))
obj = student(name, subject1, subject2, subject3)

obj.average()
