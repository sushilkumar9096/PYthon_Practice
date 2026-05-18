"""class Student:
    name = "Sumit"
    def __init__(self, student_name, car_name):
        self.name = student_name
        self.model = car_name
    def Welcome(self):
        print("Welcome Student", self.name)


print(Student.name)
s1 = Student("Sushil", "BMW")
print(s1.name)
print(s1.model)
print(s1.Welcome())

s2 = Student("Rahul", "Audi")
print(s2.name)
print(s2.model)
print(Student.name)"""




# create student class that takes  names and marks of 3 subjects as arguments in constructor  then create amethod to print average 
class Student:
    def __init__(self):
        self.mark1 = int(input("Enter mark1: "))
        self.mark2 = int(input("Enter mark2: "))
        self.mark3 = int(input("Enter mark3: "))
        self.name = input("Enter name: ")
    
    def average(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        print("Average mark of", self.name, "is", avg)
s1 = Student()
print(s1.name, s1.mark1, s1.mark2, s1.mark3)
s1.average()        