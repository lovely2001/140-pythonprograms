#Print all prime number in an interval 1 - 10

for i in range(2,11):
    ans = 1
    for j in range(2,i):
        if i%j==0:
            ans=0
            break

    if ans==1:
        print(i)

