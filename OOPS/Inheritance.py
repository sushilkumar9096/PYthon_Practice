
class A:
    varA = "I am class A variable"

class B:
    varB = "I am class B variable"

class C(A, B):
    varC = "I am class C variable"
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)







"""  class Car:
    @staticmethod
    def Start():
        print("car started")

    @staticmethod
    def Stop():
        print("car stopped")
        
class Toyata(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortunar(Toyata):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

car1 = Fortunar("Toyota", "SUV")

print(car1.brand)
print(car1.type)

car1.Start()
car1.Stop() """


