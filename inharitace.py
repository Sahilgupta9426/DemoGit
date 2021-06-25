#
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog22(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", "python")
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])

print(karan.languages)

print(shubham.languages)


# A Python program to demonstrate inheritance
#
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
# class Person:
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#     # To get name
#     def getName(self):
#         return self.name
#
#     # To check if this person is an employee
#     def isEmployee(self):
#         return False
#
#
# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):
#
#     # Here we return true
#     def isEmployee(self):
#         return True
#
#
# # Driver code
# emp = Person("Geek1")  # An Object of Person
# print(emp.getName(), emp.isEmployee())
#
# emp = Employee("Geek2")  # An Object of Employee
# print(emp.getName(), emp.isEmployee())
#
#
#




