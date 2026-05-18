"""class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.cluth = False

    def start(self):
        self.acc = True
        self.brake = False
        self.cluth = False
        print("Car is started")
s1 = Car()

s1.start() """

# create account class with 2 attribute - balance and acc number and create mmethod debit credit and printing balance after each transaction

class Account:
    def __init__(self):
        self.balance = 100
        self.accountnumber = int(input("Enter account number: "))

    def debit(self):
        amount =int(input("Enter amount to debit:  "))
        if(self.balance >= amount):
            self.balance -= amount
            print("successfully debited")
          
        else:
            print("Insufficient balance")    

    def credit(self):
        credit = int(input("Enter amount to credit: "))
        self.balance += credit
        print("successfully credited")
      
    def CheckBal(self):
        print("Your current balance is: ", self.balance)

B = Account()
print("enter 1 to debit,\n Enter 2 to credit \n Enter 3 to check balance")        
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        B.debit()
    elif choice == 2:
        B.credit()
    elif choice == 3:
        B.CheckBal()
    else:
        print("Invalid choice")