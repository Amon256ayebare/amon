class Person:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name: str, age: str, section: str):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f"Name: {self.name}, Age: {self.age}, Section: {self.section}")

# Creating a Student object
student = Student("Amon ayebare", "25", "A1")

# Testing the displayStudent method
student.displayStudent()
