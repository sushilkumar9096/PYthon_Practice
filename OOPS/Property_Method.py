class Student:
    def __init__(self, phy,math,che):
        self.phy = phy
        self.math = math
        self.che = che

    @property
    def percentage(self):
        return str(( self.phy + self.math + self.che)/ 3) + "%"


s1 = Student(90,78,89)
print(s1.percentage)
s2 = Student(56,67,89)
print(s2.percentage)