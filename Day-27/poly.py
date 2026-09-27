class Netflix:
    def __init__(self,name):
        print(f'Welcome to the netflix,{name}----------------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Play resume back")
    def ads(self):
        print("Ads will run")
    def quality(self):
        print("You have limited quality")
    def download(self):
        print("You cannot download")
    def login(self):
        print("single device login")

class PremiumNetflix(Netflix):
    def __init__(self,name):
        print(f'Welcome to the netflix,{name}----------------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Play resume back")
    def ads(self):
        print("Ads did not  run")
    def quality(self):
        print("You have high quality")
    def download(self):
        print("You can download")
    def login(self):
        print("Multi device login")

mitra = Netflix("mitra")
mitra.auth()
mitra.dashboard()
mitra.search()
mitra.history()
mitra.playcontrollers()
mitra.ads()
mitra.quality()
mitra.download()
mitra.login()
print()
pramod = PremiumNetflix("pramod")
pramod.dashboard()
pramod.search()
pramod.history()
pramod.playcontrollers()
pramod.ads()
pramod.quality()
pramod.download()
pramod.login()
                                         