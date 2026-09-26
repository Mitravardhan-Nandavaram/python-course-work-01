'''
def functionname(arg):
    #stsmt
    return (opt)

funtionname(para)

# GST

def gst(price):
    print("original price:",price)
    print("Final price:",price+price*0.18)

gst(1000)
gst(5000)
gst(800)
gst(500)  

# Maths Tables

def table(n):
    print(f"{n}-Table")
    print('------------------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)
  
#Leap year
def is leap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a Leaf Year"

print(isleap(2012))
print(isleap(2020))
print(isleap(2026))  

#Primenumbers 
n = int(input("Enter a number: "))

def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return "Not a Prime Number"

    return "Prime number"

print(isprime(16))
print(isprime(17))
print(isprime(21))
print(isprime(20))
print(isprime(19))


def display(name,email,pwd):
    print("name:",name)
    print("pwd:",pwd)

display(name'Mitra','Mitra@gmail.com','Mitra$8498')
display('Mitra@gmail.com','Mitra','Mitra$8498')
display('Mitra$8498','Mitra$gmail.com','Mitra')    

def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display(name='Mitra',email='Mitra@gmail.com',pwd='Mitra$8498')
display(email='Mitra@gmail.com',name='Mitra',pwd='Mitra$8498')
display(pwd='Mitra@8498',email='Mitra@gmail.com',name='Mitra')

def display(name,email,pwd=None):
    print("name:",name)
    print("name:",name)
    print("pwd:",pwd)

display("Mitra","email")
display("Mitra","email","pwd$8498")    


def display(*names):
    print(names)

display("Mitra")
display("Mitra","Venky")
display("Mitra","Venky","pramod")
display("Mitra","Venky","pramod","Ram")    

'''
def display(**names):
    print(names)

display(n1="Mitra")
display(n1="Mitra",n2="Venky")
    