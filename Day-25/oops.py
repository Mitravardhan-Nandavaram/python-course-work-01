'''
#Oops key points :
1.class is blueprint of objects.
2.object is instance of a class.
3.method means ‘function’ defined inside a class.
4.Attribute means ‘variable’ associated with an object of a class.
Four Main Pillers of OOPs:
Encapsulation: combining data and methods inside a class
Inheritence: Creating a new class from an existing class.
Polymoriphism:One interface can have different behaviours. 
Ex-parent class ,child class,grandchild class like.
Abstraction:Hiding unnecessary implementation details .
  Ex-password,phonepay


class Zomato:
    pass


Mitra = Zomato()
Pramod = Zomato()
supri = Zomato()


class Zomato:
    discount = 25
    def info(self,name,phoneno,adress):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Zomato',self.name)


Mitra = Zomato()
Mitra.info('Mitra',8498065355,'hyd')
Pramod = Zomato()
Pramod.info('Pramod',8408065344,'Nandyal')
Supri = Zomato() 
Supri.info('Supri',6303985722,'Banglore')

'''
Class Zomato:
    discount = 25

    @classmethod
    def updatediscount(cls):
        cls.discount = 30
        print("Update Discount:",cls.discount)

    def info(self,name,phoneno,adress):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'Welcome to the Zomato',self.name)

    @staticmethod
    def banner():
        print(f"{Zomato.discount}% is going,grab the products")


Mitra = Zomato()
Mitra.info('Mitra',8498065355,'Hyd')
Mitra.updatediscount()
Mitra.banner()


Supri = Zomato()
Supri.info('Supri',6303985722,'Banglore')
Supri.updatediscount()
Supri.banner()


Pramod = Zomato()
Pramod.info('Pramod',8498065355,'Nandyal')
Pramod.updatediscount()
Pramod.banner()

