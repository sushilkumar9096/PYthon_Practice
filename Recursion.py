"""def show(n) :
   if n == 0:
        return
   print(n)
   show(n-1)
n = int(input("Enter a number: "))
show(n)   """


# Write a recursive function to calculate the sum of first n natural elements in a list

listt =[1,2,3,4,5,6,7,8,9,10]

def Print_list(listt) :
    if(len(listt) == 0):
        return
    print(listt[0])
    Print_list(listt[1:])
Print_list(listt)