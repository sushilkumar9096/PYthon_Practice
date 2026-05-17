"""veggies = ["tomato", "potato", "onion", "carrot", "cabbage"]
for val in veggies:
    print(val)

tupple = (1, 2, 3, 4, 5)
for val in tupple:
    print(val)

str = "Hello World"
for val in str:
    if (val == 'W'):
     print("Value found: " + val)
     break
    print(val)        
"""

#wap to print the element of the follwing list using loop 
"""listt = [1,4,9,24,36,81,100]

for val in listt :
    print(val)"""

#wap to search a number x in this tuple using loops
"""
tuplee = (1, 4, 9, 24, 36, 81, 100)
x = int(input("enter a number to found :"))

for val in tuplee :
    if(val == x):
        print(str(x) + " Number found in tuple")
        break"""

#wap to find the factorial of  number n using loops        

 
n = int(input("Enter a number: "))
idx =n
fact = 1
while idx > 0 :
    fact *= idx
    idx -= 1
print("The factorial of " + str(n) + " is : " + str(fact))