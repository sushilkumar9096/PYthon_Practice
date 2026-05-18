class Account:
    def __init__(self, balance):
        self.balance = balance
        self.accountnumber =  int(input("Enter account number: "))
        self._Pass = input("Enter password: ")

    
acc = Account(100)
print(acc.balance)
print(acc.accountnumber)
print(acc._Pass)  # to access protected variable we have to use _classname__variablename