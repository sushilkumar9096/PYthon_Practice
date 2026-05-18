#del keyword use 
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

s1 =Student("Sumit", 90)
print(s1.name, s1.mark)
del s1.mark
print(s1.name)        
del s1
print(s1.name)