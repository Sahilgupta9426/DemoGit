class A:
    cvar="I am class A"
    def __init__(self):
        self.var1="I am Inside Class A construcor"
        self.cvar="instance variable class A"
        self.special="this is special variable in Class A"
class B(A):
    cvar="I am class B "
    def __init__(self):
        self.var1="I am Inside Class B construcor"
        self.cvar="instance variable class B"
        super().__init__()
a=A()
b=B()
print(b.special)