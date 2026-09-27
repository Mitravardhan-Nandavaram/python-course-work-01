from abc import ABC,abstractmethod

class payment(ABC):
    def source(self):
        print("Scanner/upiid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("select the Bank")
    def pin(self):
        print("Enter the pin")
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Success/fail")
            
        
class HDFC(payment):
    def paymentprocess(self):
        print("Payment is process through HDFC Bank")

class UNION(payment):
    def Paymentprocess(self):
        print("payment is process through UNION Bank")                


class ICICI(payment):
    def Paymentprocess(self):
        print("payment is process through ICICI Bank")         


class ANDHRABANK(payment):
    def Paymentprocess(self):
        print("payment is process through  ANDHRABANK bank")


Mitra = HDFC()
Mitra.source()
Mitra.amount()
Mitra.bank()
Mitra.pin()
Mitra.paymentprocess()
Mitra.paymentstatus()

pramod = HDFC()
pramod.source()
pramod.amount()
pramod.bank()
pramod.pin()
pramod.paymentprocess()
pramod.paymentstatus()