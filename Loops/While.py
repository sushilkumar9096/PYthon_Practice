"""count = 1
while count<= 5 :
    print(count)
    count +=1

print("loop ended")

i = 1
while i  <= 100  :
   print("\nHeloo" + str(i))
   i +=1

print("loop ended")

#wap to prit 100 - 1 numbers in reverse order
j = 100
while j>=1 :
    print(j)
    j -=1

    print("loop ended")

# print the multiplication table of anumber n

n=input("Enter a number: ")
i = 1
while i <=10 :
  print(str(n) + " x " + str(i) + " =  " +str(int(n)*i))
  i +=1

  print("loops eneded") 

#print the elements of a list using while loop
listt = [1, 2, 3, 4, 5]
idx = 0
while idx <= len(listt)-1 :
    print(listt[idx])
    idx +=1

    print("loop ended")"""

"""#wap to search a number of x in this tuples using loops

tupp = (1,2,3,4,5,6,7,8,9,5,10)

x = int(input("Enter a number to search: "))

idxx = 0

while idxx <= len(tupp)-1:

    if x == tupp[idxx]:
        print(str(x) + " Number found at index " + str(idxx))
        

    idxx += 1"""

#wap to  fing the sum of  n numbers using while loop

n = int(input("Enter a number: "))

idxx = 0
sum =0
while idxx <= n :
    sum += idxx
    idxx += 1
print("The sum of first " + str(n) + " numbers is : " + str(sum))