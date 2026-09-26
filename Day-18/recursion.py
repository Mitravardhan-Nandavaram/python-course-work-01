# recursion means function call itself again and  until condition stops it
'''
def fun(arg):
    if base:
        return
    fun(update arg)
fun(para)    

def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display                

def display(n):
    if n==0:
        return
    print(n)
    display(n-1)

display(10)   
''' 
def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)

display("Mitravardhan",0)        

