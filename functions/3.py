def passorfail(m):
    if(mark>80):
        print("good")
    elif(mark<80 or mark>50):
        print("avg")
    else:
        print("fail")
mark=int(input("mark="))
passorfail(mark)