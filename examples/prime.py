# n=int(input("num="))
# if(n<=1):
#     print(f"{n} invalid number")
# elif(n%2 == 1):
#     print("prime",n)

# else:
#     print("no",n)
n=int(input())
fact=1
for i in range(n):
    fact=fact*n
    n=n-1

print(fact)