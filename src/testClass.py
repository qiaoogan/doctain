class Person:

    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}({self.age}) is living in {self.city}'

    def myFunction(self,city):
        self.city = city


P1 = Person("John",30)
P1.myFunction("new york")
print(P1)

class Student(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year = year

S1 = Student("Mike",25,2023)
print(S1.year)