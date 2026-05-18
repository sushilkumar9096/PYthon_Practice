class Account:

    __name = "Sumit"  # private variable
    def __init__(self, balance):
        self.balance = balance
        self.accountnumber =  int(input("Enter account number: "))
        self.__Pass = input("Enter password: ")

    def __hello(self):
        print("Hello")    

    def welcome(self):
        print("Welcome", self.__name)
        self.__hello()

    
acc = Account(100)
acc.welcome()
print(acc._Account__hello())  # to access private method we have to use _classname__methodname
print(acc.balance)
print(acc.accountnumber)
print(acc._Account__Pass)  # to access private variable we have to use _classname__variablename