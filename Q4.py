#Program to swap 2 variables

number1 = int(input("Enter number 1 : "))
number2 = int(input("Enter number 2 : "))

print(f"Before swapping : {number1} and {number2}")

temp = number1
number1 = number2
number2 = temp

print(f"After swapping : {number1} and {number2}")