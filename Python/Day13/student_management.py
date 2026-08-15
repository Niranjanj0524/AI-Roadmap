class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Course: {self.course}"

class GraduateStudent(Student):
    def __init__(self, student_id, name, age, course, thesis_topic):
        super().__init__(student_id, name, age, course)
        self.thesis_topic = thesis_topic

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_students(self):
        print("\n --- Add Student ---")
        print("1. Regular Student")
        print("2. Graduate Student")

        student_type = input("Select student type (1-2): ").strip()

        student_id = input("Enter student id : ").strip()

        for student in self.students:
            if student.student_id == student_id:
                print("Error: Id already present")

        name = input("Enter Name: ").strip()
        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("Invalid entry for age")
            return

        course = input("Enter Course: ").strip()

        if student_type == '2':
            thesis_topic = input("Enter Thesis Topic: ").strip()
            new_student = GraduateStudent(student_id, name, age, course, thesis_topic)
        else:
            new_student = Student(student_id, name, age, course)
            
        self.students.append(new_student)
        print(f"Student added successfully!")

    def view_students(self):
        print("\n --- View Student ---")
        if not self.students:
            print("No student record found.")
            return

        for student in self.students:
            print(student.introduce())

    def search_student(self):
        search_id = input("Enter Id for search: ")

        for student in self.students:
            if student.student_id == search_id:
                print("Student found.")
                print(student.introduce())
                return

        print("Student record not found.")


if __name__ == "__main__":
    system = StudentManagement()
    
    while True:
        print("\n===============================")
        print("   STUDENT MANAGEMENT MENU     ")
        print("===============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            system.add_students()
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            system.search_student()
        elif choice == '4':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please select 1, 2, 3, or 4.")