class goa():
    drink=""
    name=""
    def party(self):
        print("lets party")
    def beach(self):
        print("beach...")
rk=goa()
dh=goa()
rk.name="rk"
rk.drink="no"
dh.name="dharni"
dh.drink="yes"
print(rk.name,"drink :",rk.drink)
rk.party()

print(dh.name,"drink :",dh.drink)
dh.beach()