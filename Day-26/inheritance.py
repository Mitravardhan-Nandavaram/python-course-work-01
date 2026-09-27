''''''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self): 
        print("You can upload the status for 24hrs") 

class whatsappv3:
    def groups(self):
        print("You can create the groups ")  

class whatsappv4:
    def calls(self):
        print("You can call and talk with multiple people")  

class whatsappv5:
    def  community(self):
        print("You can access multiple groups")

class whatsappv6(whatsappv4,whatsappv5,whatsappv2):
    def  channels(self):      
        print("You can post with huge crowd")                 

mitra = whatsappv1()
mitra.message()  
mitra = whatsappv2()
mitra.status()   
mitra = whatsappv3()
mitra.groups()
mitra = whatsappv4()
mitra.calls()
mitra = whatsappv5()
mitra.community()
mitra = whatsappv6()
mitra.channels()


class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self): 
        print("You can upload the status for 24hrs") 

class whatsappv3(whatsappv1):
    def groups(self):
        print("You can create the groups ")  

class whatsappv4(whatsappv1):
    def calls(self):
        print("You can call and talk with multiple people")  

class whatsappv5(whatappv1):
    def  community(self):
        print("You can access multiple groups")

class whatsappv6(whatsappv5,whatsappv4,whatsappv3,whatsappv2,whatsappv1):
    def  channels(self):      
        print("You can post with huge crowd")  

mita =whatsappv6()
mitra.message()
mitra.status()
mitra.groups()
mitra.calls()
mitra.community()
mitra.channels()    

'''
  