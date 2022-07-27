# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    def __init__(self, name, email, age ):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"{self.name} is {self.age} years old"


sami = User("Sami", "freelancersami123@gmail.com", 16)
print(sami.greeting())
