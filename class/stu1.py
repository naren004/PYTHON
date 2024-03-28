class student:
    def __init__(self):
        self.name=''
        self.reg=''
    def display(self):
        print("NAME :",self.name)
        print("REG NO : " ,self.reg)
stu1=student()
stu2=student()

stu1.name="naren"
stu1.reg="35"

stu2.name="karthi"
stu2.reg="27"

stu1.display()
stu2.display()