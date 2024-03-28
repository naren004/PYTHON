s_useranme="naren"
s_password="123"
uname=input("NAME")
password=input("PASSWORD")
def fun():
    if (uname==s_useranme and password==s_password):
        return True
    else:
        return False
# func=fun()
print(fun()) 