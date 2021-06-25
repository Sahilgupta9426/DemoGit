class Employee:
    # var=6
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

class Player:
    var=7
    no_games=4
    def __init__(self , name,game):
        self.name=name
        self.game=game
    def printdet(self):
        print(self.name,self.game)
        # return f"The Name is {self.name}. game is {self.game}"


class Coolprog(Player,Employee):
    var=99
    lang="java"
    def printaaa(self):
        print(self.lang)

# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
# player1=Coolprog("sahil" , 7777,"jhjh")


player1=Coolprog("sahil" , "cricket")
player1.printdet()
# print(player1.var)
# player1.printaaa()
print(Coolprog.var)

player2=Coolprog("abhay","gupta")
player2.printaaa()