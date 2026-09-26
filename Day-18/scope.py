#scope of variables
#Local variable:a variable can perform only Inside function 
'''
def display():
    n=10
    print("Inside function:"n)
    display()
    print("outside function:",n)

#Global variable:a variable can perform Inside and Outside 
def display():
    print("Inside function:",n) 

n=10
display()
print("Outside function:",n)

# It can perform local and Global variable
def display():
    global n
    n=10
    print("Inside function:",n)

display()
print("Outside function:",n)

#

def display():
    global n
    n+=10
    print("Inside function:",n)


n=10
display()
print("Outside function:",n)


def display():
    course ="python"
    def update():
        nonlocal course
        course ="java"
        print("Inside function:",course)
    update()
    print("Outside function:",course)

display()

#built in fuction:fun act as a variable

l = [1,2,3,4,5]
print(max(l))

print = 20
print(max)

'''


