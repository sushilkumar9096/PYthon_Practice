class Student:
    def __init__(self):
        self.__name = ""

    # Setter
    def set_name(self, name):
        self.__name = name

    # Getter
    def get_name(self):
        return self.__name


s1 = Student()

s1.set_name("Sushil")

print(s1.get_name())