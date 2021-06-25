# class A:
#     def __init__(self):
#         self.name="sahil"
#         self.game="cricket"
#     def sahil(self):
#         return self.name
#
# class B:
#     def __init__(self):
#         self.name="sahil B"
#         self.game="cricket"
#     def sahil(self):
#         return self.name
#
#
# class C(A,B):
#     def __init__(self):
#         self.name="sahil"
#         super().__init__()
#     def sahil(self):
#         return self.name ,self.game
# h1=B()
# print(h1.sahil())


class A:
    var="class A "
    def __init__(self):
        self.var="class A intance"
class B(A):
    var = "class B "

    def __init__(self):
        self.var = "class B intance"

class C(B):
    var = "class C "

    # def __init__(self):
    #     self.var = "class C intance"
obj1=C()
print(obj1.var)

