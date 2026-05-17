"""def sum(a,b):
    return(a+b)

a=eval(input("Enter a number: "))
b=eval(input("Enter a number: "))
print(sum(a,b))
"""

# wap to to print length of list using function

listt = [1, 2, 3, 4, 5]
ciites = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
heros = ["Superman", "Batman", "Spiderman", "Ironman", "Thor"]
vilolan = ["Joker", "Thanos", "Loki", "Green Goblin", "Ultron"]

"""def print_Len(list) :
    return len(list)

print(print_Len(listt))
print(print_Len(ciites))
print(print_Len(heros))
print(print_Len(vilolan))

"""
# wap to print te elments of a list in a single line using function

"""def single_line(list) :
    for val in list :
        print(val , end = " , ")
    print()
single_line(listt)
single_line(ciites)"""

#wap to find factorial of n number using function



n = int(input("Enter a number: "))

def fact(n):

    if n < 0:
        return "Enter a positive number"

    factt = 1

    for i in range(1, n + 1):
        factt *= i

    return factt


print("The factorial of " + str(n) + " is : " + str(fact(n)))