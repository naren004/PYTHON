a=[]
n=int(input("n="))
for i in range(1,n+1):
    a.append(i)
print(f"the first {n} natural numbers ")
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)