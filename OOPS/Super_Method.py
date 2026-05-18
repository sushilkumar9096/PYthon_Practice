class Car:
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type
    @staticmethod
    def Start():
        print("car started")

    @staticmethod
    def Stop():
        print("car stopped")
        
class Toyata(Car):
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type


