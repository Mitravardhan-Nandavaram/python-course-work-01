class Redbus:
    bus = {i: "Available" for i in range(1,11)}

    def displayseats(self):
        print("Zing Bus")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])

    def booking(self,seatno):
        for  i in Redbus.bus:
         if i == seatno and Redbus.bus[i] == 'Available':
            Redbus.bus[i] = 'Booked'
            print(f"Your seat - {seatno} is successfully booked")
            break
        else:
            print(f"Your seat - {seatno} is already Booked")

class User(Redbus):
    def __init__(self,name,email,phoneno):
        self.name = name
        self.email = email
        self.phoneno = phoneno
        print(f"Hello {self.name}, Welcome to the Redbus")

Mitra = User('Mitra','mitravardhan35@gmail.com',8498065355)
Mitra.displayseats()
Mitra.booking(7)
Mitra.displayseats()
Mitra.booking(7)