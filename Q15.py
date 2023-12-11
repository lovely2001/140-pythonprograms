#program to check whether the number is prime or not

number = int(input("Enter the number : "))

if number ==  1:
    print(f"{number} is not a prime number")
    
ans = 1
for i in range(2,number):
    if(number % i == 0):
        ans=0
        print("Not a prime number")
        break

if ans==1:
    print("It is a prime number")