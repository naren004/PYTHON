class student():
    def __init__(self):
        self.name=""
        self.reg=()
    def display(self):
        print(self.name)
        print(self.reg)
it=student()
cs=student()
ece=student()
it.name="abi"
cs.name="leo"
ece.name="star"
it.reg=12
cs.reg=90
ece.reg=555
it.display()
cs.display()
ece.display()