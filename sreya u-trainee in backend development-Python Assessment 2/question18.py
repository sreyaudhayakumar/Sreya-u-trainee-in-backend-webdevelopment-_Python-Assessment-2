"""18. Python program to for student height record for a school using Class and
Objects."""

class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, height):
        self.students.append(Student(name, height))

    def display_height_records(self):
        print("Student Height Records:")
        for student in self.students:
            print(f"{student.name}: {student.height} cm")

def main():
    school = School()
    stud1=input("enter the name:")
    stud1_height=int(input("enter the height:"))
    stud2=input("enter the name:")
    stud2_height=int(input("enter the height:"))
    stud3=input("enter the name:")
    stud3_height=int(input("enter the height:"))



    school.add_student(stud1,  stud1_height)
    school.add_student(stud2, stud2_height)
    school.add_student( stud3, stud3_height)

    school.display_height_records()

if __name__ == "__main__":
    main()

