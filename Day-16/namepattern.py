
''''
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i ==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()              
#E
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() 

n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j== 0  or i == m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() 

n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j== 0  or i == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()         

n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j== 0  or i == n-1 or (j==n-1 and i>=m) or (i==m and j>m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()             
# Z
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  j== 0 or i==m or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()            
# x
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  i==0 or i == n-1 or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()                
# Y
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  i==j or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()         
# J
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  i==0 or j==m or (j<=m and i==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()         
# K
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  j==0 or (i==m and j<=m) or (i==j  and i>=m) or (i+j == n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()           
# M
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()         
# w 
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1 or (i==j and i>=m) or (i+j==n-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()         
# v
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()         
# L
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  i==0 or j==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()         
# T
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if  j==0 or i==0 or (j==n-1 and i<=m) or i==m or (i==j and i>=m):
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()         
 
# R
n = int(input("Enter the size"))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or  
            print('*',end=' ') 
        else:
            print(' ',end=' ')
    print()             


