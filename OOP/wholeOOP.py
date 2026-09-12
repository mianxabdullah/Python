# UNIVERSITY MANAGEMENT SYSTEM
# Import tools to create abstract classes
from abc import ABC, abstractmethod

# ===== ABSTRACT CLASS (Abstraction) =====
class Person(ABC):
    def __init__(self, name, age):
        self.name = name                # Public attribute
        self._age = age                 # Protected attribute (by convention)
        self.__national_id = id(self)  # Private attribute (name mangled to prevent direct access)

    @abstractmethod
    def get_role(self):
        pass  # Abstract method, must be overridden in subclasses

    def get_national_id(self):
        return self.__national_id  # Public getter for private attribute

    def __str__(self):  # Operator overloading for readable printing
        return f"{self.get_role()}: {self.name}, Age: {self._age}"


# ===== MULTIPLE INHERITANCE EXAMPLE =====
class Researcher:
    def __init__(self, field):
        self.field = field  # Field of research

    def research_topic(self):  # Regular method
        return f"Researching in {self.field}"


# ===== SINGLE INHERITANCE (Student inherits Person) =====
class Student(Person):
    student_count = 0  # Class variable shared among all Student objects

    def __init__(self, name, age, student_id, gpa):
        super().__init__(name, age)       # Call parent constructor
        self.student_id = student_id      # Unique ID for student
        self.gpa = gpa                    # Student's GPA
        Student.student_count += 1        # Increment shared counter

    def get_role(self):
        return "Student"  # Override abstract method from Person

    def __add__(self, other):  # Operator overloading to add two GPAs
        return (self.gpa + other.gpa) / 2

    @classmethod
    def total_students(cls):  # Access class-level data
        return cls.student_count

    @staticmethod
    def is_passing(gpa):  # Independent utility method
        return gpa >= 2.0


# ===== MULTILEVEL + MULTIPLE INHERITANCE (GraduateStudent) =====
class GraduateStudent(Student, Researcher):
    def __init__(self, name, age, student_id, gpa, thesis_topic, field):
        Student.__init__(self, name, age, student_id, gpa)  # Call constructor of Student
        Researcher.__init__(self, field)                    # Call constructor of Researcher
        self.thesis_topic = thesis_topic                    # Additional attribute

    def get_role(self):  # Override get_role again
        return "Graduate Student"

    def __str__(self):  # Override print method to include thesis
        return super().__str__() + f", Thesis: {self.thesis_topic}"


# ===== ANOTHER CHILD CLASS OF PERSON (Teacher) =====
class Teacher(Person):
    def __init__(self, name, age, emp_id, subject):
        super().__init__(name, age)  # Initialize base class
        self.emp_id = emp_id         # Unique employee ID
        self.subject = subject       # Subject being taught

    def get_role(self):
        return "Teacher"  # Override abstract method


# ===== COMPOSITION + AGGREGATION EXAMPLE (Course) =====
class Course:
    def __init__(self, title, teacher):
        self.title = title           # Course title
        self.teacher = teacher       # Composition: course "owns" the teacher
        self.students = []           # Aggregation: holds references to students

    def add_student(self, student):  # Aggregation: student added externally
        self.students.append(student)

    def course_info(self):  # Print full course details
        info = f"Course: {self.title}, Taught by: {self.teacher.name}\n"
        info += "Enrolled Students:\n"
        for s in self.students:
            info += f"  - {s.name} (GPA: {s.gpa})\n"
        return info


# ===== FRIEND-LIKE FUNCTION (Python doesn’t support real friends) =====
def show_personal_info(person):
    # Accesses public method to get private data
    print(f"Name: {person.name}, National ID: {person.get_national_id()}")


# ===== MAIN PROGRAM EXECUTION =====
if __name__ == "__main__":
    # Create a Teacher
    t1 = Teacher("Dr. Smith", 50, "T101", "AI")

    # Create Students
    s1 = Student("Ali", 20, "S001", 3.5)
    s2 = Student("Zara", 19, "S002", 3.8)

    # Create a Graduate Student (inherits Student + Researcher)
    gs1 = GraduateStudent("Usman", 24, "GS001", 3.7, "AI Ethics", "Artificial Intelligence")

    # Create a Course and add Students
    course1 = Course("Machine Learning", t1)
    course1.add_student(s1)     # Add student (Aggregation)
    course1.add_student(gs1)    # Add graduate student (Aggregation)

    # Demonstrate Polymorphism (get_role overridden in each subclass)
    print(t1)    # Teacher object printed using __str__()
    print(s1)    # Student object
    print(gs1)   # GraduateStudent with thesis info
    print()

    # Display course info (Composition + Aggregation)
    print(course1.course_info())

    # Operator Overloading (add two Student objects)
    print(f"Average GPA (Ali + Zara): {s1 + s2}")

    # Show use of class and static methods
    print("Total Students:", Student.total_students())        # Class method
    print("Is Zara passing?", Student.is_passing(s2.gpa))     # Static method

    # Demonstrate Multiple Inheritance
    print("Graduate Student Research:", gs1.research_topic())

    # Simulate friend function accessing private data via getter
    show_personal_info(s1)

    # Destructor example (in Python __del__ is not reliable)
    del s2  # Optional: calls __del__ if defined

