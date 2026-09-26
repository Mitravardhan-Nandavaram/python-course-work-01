#str list tuple set  dict range 

#for var in seq: 
    #stmts
'''
s = 'python programming' 
for i in s: 
     print(i) 

l = [1,2,3,4,5] 
for num in l: 
    print(num) 


prices = (9876,4567,567,321) 
for price in prices: 
    print(price) 
     
names = {'mitra','ranjith','rasool',} 
for name in names: 
    print(name) 
d = {1:2,2:4,3:6,4:8,5:10} 
for i in d: 
    print(i,d[i]) 

 #range(start,end+1,step):(0,,1)
for i in range(1,11):
     print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,0,-2):
    print(i)

s = 'Java Programming'
for i in  range(len(s)):
    print(i,s[i])

s = (456,4567,4567,543,3456)
for i in range(len(s)):
    print(i,s[i])

s = [6789,6789,5678,4567,3456]
for i in enumerate(s):
    print(i[0],i[1])

d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])

for i in range(1,15):
    if i==6:
        break
        print(i)

for i in range(1,15):
    if i==6:
        continue
        print(i)

for i in range(1,15):
    if i==6:
        break
        print(i)
else:
    print("End of Loop")

l = [12,13,15,16,17,18,19,20] 
n=26
for i in l:
    if i == n:
        print(n,"found")
        break
else:
    print(n,"not found")

pin = 1234
for i in range(3):
    epin = int(input("Enter the pin:"))
    if epin == pin:
        print("Unlock phone")
        break
    else:
        print("Incorrect pin")
else:
    print("Try again after 30 seconds")

n = 10
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")        
                
        
                      