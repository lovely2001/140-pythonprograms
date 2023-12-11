#swap two variables with out using temp

number1 = int(input("Enter number1 : "))
number2 = int(input("Enter number2 : "))

number1 , number2 = number2, number1

print(f"After swapping : {number1} , {number2}")

