class Student:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __str__(self):
        return f"{self.first_name} {self.last_name}, ID={self.id}"

    def say_hello(self):
        return f"{self.first_name} {self.last_name} says Hi!"


student1 = Student("John", "Smith", 1)

print(student1)

student1.say_hello()



pass
