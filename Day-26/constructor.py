'''
class Whatsapp:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"welcome to Whatsapp, {self.username}")

Mitra = Whatsapp('Mitra','8498065355') 


class Instagram:
    def __init__(self,username,password):
        self.username =username
        self.__password = password
        self.__post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._post 

Mitra = Instagram('Mitra','849806')

print(Mitra.username)
print(Mitra.getpassword())
print(Mitra.accesspost)

'''
class Instagram:
    def __init__(self,username,password):
        self.username =username
        self.__password = password
        self.__post = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword  

    @property
    def accesspost(self):
        return self._post 

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)    

Mitra = Instagram('Mitra','849806')

print(Mitra.username)
print(Mitra.getpassword())
print(Mitra.accesspost)

Mitra.username = 'Mitra_123'
print(mitra.username)

Mitra.setpassword('mitra##123')
print(mitra.getpassword())

Mitra.accesspost = 'python intro'
Mitra.accesspost = 'string'
Mitra.accesspost = 'project'

