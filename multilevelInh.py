class Dad:

    var=1
    bask=1111
    # def __init__(self ,name ,game ):
    #     self.name=name
    #     self.game=game


    def printdet(self):
        return f"name and game of class dad is {self.var} "

class son(Dad):
    bask = 99
    # var=9
    # def __init__(self ,name ,game):
    #     self.name=name
    #     self.game=game

    def printdet(self):
        return f"name and game of class son  is {self.var} "


class grandson(son):
    # var=55
    # def __init__(self ,name ,game):
    #     self.name=name
    #     self.game=game

    def printdet(self):
        return f"name and game of class grandson is {self.var} "


obj1=grandson()
print(obj1.printdet())
print(obj1.bask)