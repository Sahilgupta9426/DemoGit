# class emp:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{self.fname}.{self.lname}@django.com"
#
#     def explain(self):
#         return f"first name {self.fname} last name {self.lname}"
#     @property
#     def printmail(self):
#         return f"{self.fname}.{self.lname}@django.com"
#
#
# hind_supp=emp("sahil","gupta")
# obj2=emp("sahil","gupta")
# print(hind_supp.explain())
# print(hind_supp.printmail)
# hind_supp.fname="abhay"
# print(hind_supp.explain())
# print(hind_supp.printmail)

class emp:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@django.com"

    def explain(self):
        return f"first name {self.fname} last name {self.lname}"
    @property
    def printmail(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@django.com"
    @printmail.setter
    def printmail(self,string):
        print("Setting now...")
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]
    @printmail.deleter
    def printmail(self):
        self.fname=None
        self.lname=None

hind_supp=emp("sahil","gupta")
obj2=emp("sahil","gupta")
print(hind_supp.printmail)
hind_supp.printmail="sahil.kuchbhi@gmail.com"
print(hind_supp.lname)

del hind_supp.printmail
print(hind_supp.printmail)
