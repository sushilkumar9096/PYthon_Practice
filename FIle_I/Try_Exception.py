
# TRY AND EXCEPT


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except:
    print("Some error occurred")



# MULTIPLE EXCEPTIONS


try:
    num = int(input("\nEnter a number: "))

    result = 10 / num

    print("Result =", result)

except ValueError:
    print("Please enter only numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")



# CUSTOM EXCEPTION


class NegativeNumberError(Exception):
    pass


try:

    age = int(input("\nEnter age: "))

    if age < 0:
        raise NegativeNumberError("Age cannot be negative")

    print("Age is:", age)

except NegativeNumberError as e:
    print(e)



# FINALLY BLOCK


try:

    f = open("2.py", "r")

    print("\nFile opened successfully")

except FileNotFoundError:
    print("File not found")

finally:
    print("Finally block always executes")

    try:
        f.close()
        print("File closed")

    except:
        pass