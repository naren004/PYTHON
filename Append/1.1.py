a=[]
for i in range(1,6):
    num=int(input("enter num"+str(i)))
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
print("sum >",sum)
avg=sum/i
print("avg",avg)
print(i)