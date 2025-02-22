class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
# Creación de persona y saludo
person1 = Person("Juan", 31)
person1.greet()
print(person1)
print(repr(person1))

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet
        print(f"Y soy estudiente con ID: {self.student_id}")

#Creación de estudiante
student1 = Student("Juan", 31, "S0001")
student1.greet()