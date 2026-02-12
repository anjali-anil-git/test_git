from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no):
        student = Student(name, roll_no)
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print("No students found")
            return

        for s in self.students:
            print(f"Roll: {s.roll_no}, Name: {s.name}")

    def save_to_file(self):
        with open("students.txt", "w") as f:
            for s in self.students:
                f.write(str(s) + "\n")

    def load_from_file(self):
        try:
            with open("students.txt", "r") as f:
                for line in f:
                    roll_no, name = line.strip().split(",")
                    self.add_student(name, roll_no)
        except FileNotFoundError:
            print("No previous data found")
