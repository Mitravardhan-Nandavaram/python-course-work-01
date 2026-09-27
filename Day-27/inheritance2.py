''''
class whatsappv1:
    def status(self):
        print("You can upload the status for 24hrs")

class Whatsappv2(Whatsappv1):
    def status(self):
        super().status()#this super method makes to access the same method used
     in parent class and print it this is only applicable if the method is same
        print("You can add music and you can react")


a = whatsappv1()
a.status()

'''

class whatsappv1:
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv2():
    def status(self):
        print("You can add music and you can react")


class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can add to the cross platfroms")

a = whatsappv3()
a.satus()     


