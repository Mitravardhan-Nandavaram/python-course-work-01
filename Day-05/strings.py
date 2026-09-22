Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #int float complex str list tuple set dict bool
>>> a = inpuut()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = inpuut()
NameError: name 'inpuut' is not defined. Did you mean: 'input'?
>>> a = input()
codegnan
>>> a
'codegnan'
>>> a = input()
12345
>>> a
'12345'
>>> a = input("Enter the value: ")
Enter the value: casegu64t37iw46yj4i237
>>> a
'casegu64t37iw46yj4i237'
>>> marks = input("Enter the marks: ")
Enter the marks: 99
>>> a
'casegu64t37iw46yj4i237'
>>> marks = input("Enter the marks: ")
Enter the marks: 123.432
>>> marks = input("Enter the marks: ")
Enter the marks: 12
>>> marks
'12'
>>> price = float(input("Enter the price: "))
Enter the price: 123.432
>>> price
123.432
>>> cgpa = float(input("Enter the cgpa: "))
Enter the cgpa: 9.9
>>> cgpa
9.9
>>> names.split()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
>>> names.
SyntaxError: invalid syntax
>>> names.split()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
names.Split()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    names.Split()
NameError: name 'names' is not defined
names = ' mitra,teja,pramod'
names.split(',')
[' mitra', 'teja', 'pramod']
courses = 'python-java-c++-flask'
courses.split('-')
['python', 'java', 'c++', 'flask']
softskills = 'communication quickleaner'
softskills.split()
['communication', 'quickleaner']
names = input("Enter the names: ").split()
Enter the names:  mitra teja pramod
name
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name
NameError: name 'name' is not defined. Did you mean: 'names'?
names
['mitra', 'teja', 'pramod']
names = tuple(input("Enter the names: ").split())
Enter the names:  mitra teja pramod
names
('mitra', 'teja', 'pramod')
names = set(input("Enter the names: ").split())
Enter the names:  mitra teja pramod
namses
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    namses
NameError: name 'namses' is not defined. Did you mean: 'names'?
names
{'pramod', 'teja', 'mitra'}
markes = input().split()
12 34 68 89 09
marks
'12'
marks
'12'
marks = input().split()
12 34 68 89 09
SyntaxError: multiple statements found while compiling a single statement
marks = input().split()
12 34 68 89 09
SyntaxError: multiple statements found while compiling a single statement
marks = input().split()
12 34 68 89 09
marks
['12', '34', '68', '89', '09']
map(int,marks)
<map object at 0x0000022647AFFF40>
list(map(int,marks))
[12, 34, 68, 89, 9]
marks = list(map(int,input("Enter the marks").split()))
Enter the marks 12 56 234 67 25 345 78
marks
[12, 56, 234, 67, 25, 345, 78]
marks = tuple(map(int,input("Enter the marks").split()))
Enter the marks 325 456 5678
marks
(325, 456, 5678)
marks = set(map(int,input("Enter the marks").split()))
Enter the marks4567 5678 46578
marks
{46578, 5678, 4567}
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"str")
a
1
b
12.3
c
'str'
email,password = input("Enter the email, password:").split()
Enter the email, password:@Mitra25
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    email,password = input("Enter the email, password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password = input("Enter the email, password:").split()
Enter the email, password:mitra25
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    email,password = input("Enter the email, password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password = input("Enter the email, password:").split()
Enter the email, password: mitra@codegnan.com 12345
email
'mitra@codegnan.com'
password
'12345'
 name,marks = input("Enter the marks"
                    
SyntaxError: unexpected indent
name,marks = input("Enter the marks").split
                    
Enter the marks56
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    name,marks = input("Enter the marks").split
TypeError: cannot unpack non-iterable builtin_function_or_method object
name,marks = input("Enter the marks").split
                    
Enter the marksmitra 99
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    name,marks = input("Enter the marks").split
TypeError: cannot unpack non-iterable builtin_function_or_method object
KeyboardInterrupt
KeyboardInterrupt
name,marks = input("Enter the marks").split
                    
Enter the marks:mitra 99
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    name,marks = input("Enter the marks").split
TypeError: cannot unpack non-iterable builtin_function_or_method object

name,marks = input("Enter the marks").split
                    
Enter the marks mitra 99
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    name,marks = input("Enter the marks").split
TypeError: cannot unpack non-iterable builtin_function_or_method object
name,marks = input("Enter the marks").split
                    
Enter the marksmitra 99
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    name,marks = input("Enter the marks").split
TypeError: cannot unpack non-iterable builtin_function_or_method object
name,marks = input("Enter the marks").split
                    
Enter the marks
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    name,marks = input("Enter the marks").split
TypeError: cannot unpack non-iterable builtin_function_or_method object
name,marks = input("Enter the marks").split()
                    
Enter the marks Mitra 99
marks
                    
'99'
int(marks)
                    
99
a,b,c= list(map(int,input().split()))
                    
12 34 45
a
                    
12
b
                    
34
c
                    
45
status = eval(input())
                    
status
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'status' is not defined
status
                    
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    status
NameError: name 'status' is not defined
status
                    
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    status
NameError: name 'status' is not defined
status
                    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    status
NameError: name 'status' is not defined
status = eval(input())
                    
true
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
status = eval(input())
                    
print(status)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
... NameError: name 'status' is not defined
... status = eval(input())
...                     
... True
... status
...                     
... True
... status=eval(input())
...                     
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> status = eval(input())
...                     
2+3j
>>> status
...                     
(2+3j)
>>> type(status)
...                     
<class 'complex'>
>>> status= eval(input())
...                     
1400
>>> status
...                     
1400
>>> status = eval(input())
...                     
[1,2,3,5]
>>> status
...                     
[1, 2, 3, 5]
>>> status = eval(input())
...                     
(8,9,5,7,)
>>> status
...                     
(8, 9, 5, 7)
>>> status = eval(input())
...                     
{1:1,2:2,3:3,4:4,5:5}
>>> status
...                     
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
>>> type(status)
...                     
<class 'dict'>
