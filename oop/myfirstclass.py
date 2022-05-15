class Person:

    num_legs = 2
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(f"{self.name} is walking")


john = Person("John", 28, "male")

print(john.age)

john.age = 31

print(john.age)

john.walk()

print(john.num_legs)