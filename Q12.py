#to check if a number is positive,negative or zero

number = int(input("Enter the number : "))

if number==0:
    print(f"Entered number is 0")

elif number > 0:
    print(f"Entered number is {number} which is positive")
else:
    print(f"Entered number is {number} which is negative")