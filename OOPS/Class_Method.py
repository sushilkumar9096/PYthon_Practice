class Person:
    name = "John"

    def changename (self,name):
        Person.name = name
        #delf.__class__.name = name  # we can also use this to change class variable

    @classmethod
    def changename1(cls,name):
      cls.name = name

p1 = Person()
print(p1.name)
p1.changename("Sumit")
print(p1.name)
print(Person.name)
Person.changename1("Alice")
print(p1.name)
print(Person.name)