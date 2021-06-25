class Empl:

    def __init__(self,name ,salary, id_number, details):
        self.name=name
        self.salary=salary
        self.id_number=id_number
        self.details=details

    def printdet(self):
        return f"my name is {self.name} and my salary is {self.salary}, my id number is {self.id_number},{self.details}"

class Player:
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def playerdet(self):
        print("player name",self.name, "and game",self.game)

# obj1=Player("ABHAY","cricket")
# obj1.playerdet()

# MULTIINHERITANCE IN COOLPROGRAMER
class CoolProgramer(Empl,Player):
    def __init__(self, post, working_hour):
        self.post=post
        self.working_hour=working_hour
    def printdet(self):
        return f" Employee Post {self.post} working hour {self.working_hour}"
# obj1=CoolProgramer("sahil","1000000000",100102,"love anime")
# print(obj1.printdet())
obj1=CoolProgramer("web developer",10)
print(obj1.printdet())