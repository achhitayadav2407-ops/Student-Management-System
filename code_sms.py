class Student:
    all_students = []

    def __init__(self, roll, name, marks):
        self.roll_number = roll
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

    def show_details(self):
        print("\nStudent Details")
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Marks       : {self.marks}")

    @classmethod
    def find_student_by_roll_number(cls, roll):
        for student in cls.all_students:
            if student.roll_number == roll:
                return student
        return None

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No student found.")
            return

        for student in cls.all_students:
            student.show_details()

    @classmethod
    def add_student(cls):
        name = input("Enter student name: ")
        roll = input("Enter student roll number: ")
        marks = int(input("Enter student marks: "))

        student = cls(roll, name, marks)
        cls.all_students.append(student)

        print(f"Student {name} added successfully!")

    @classmethod
    def update_student_marks(cls):
        roll = input("Enter student roll number to update marks: ")
        student = cls.find_student_by_roll_number(roll)

        if student:
            new_marks = int(input("Enter new marks: "))
            student.update_marks(new_marks)
            print(f"Marks for {student.name} updated successfully!")
        else:
            print("Student not found.")


def menu():
    while True:
        print("\n============= Student Management System =============")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show All Students")
        print("4. Exit")

        choice = input("Enter your option: ")

        if choice == "1":
            Student.add_student()

        elif choice == "2":
            Student.update_student_marks()

        elif choice == "3":
            Student.show_all_students()

        elif choice == "4":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
    
    
    
   