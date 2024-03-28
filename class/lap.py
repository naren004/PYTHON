class lap:
    def __init__(self):
            self.ram=""
            self.pro=""
    def display(self):
        print("RAM:",self.ram)
        print("PRO:",self.pro)

dell=lap()
hp=lap()

hp.ram="8gb"
dell.ram="4gb"
hp.pro="i3"
dell.pro="i7"

dell.display()
hp.display()
