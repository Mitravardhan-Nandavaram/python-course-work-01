#python list
Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
1 = []
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l = []
l = list()
type(l)
<class 'list'>
l= [1,12.3,"str",True,[1,2,3],(1,2,3),{1:1,2:2,3:3,},3+8j]
1
1
l= [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3,},3+8j]
1
1
l= [1,12.3,"str",True,[1,2,3],(1,2,3),{1:1,2:2,3:3,},3+8j]
l
[1, 12.3, 'str', True, [1, 2, 3], (1, 2, 3), {1: 1, 2: 2, 3: 3}, (3+8j)]
a = [1,2,3]
b = [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a=[567,76,13,433,134]
a+b
[567, 76, 13, 433, 134, 4, 5, 6]
a*b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'
a[-1]
134
a[-5]
567
a[-4]
76
a
[567, 76, 13, 433, 134]
a[1::2]
[76, 433]
a
[567, 76, 13, 433, 134]
76 in a
True
8765 in a
False
13 not in a
False
max(a)
567
min(a)
13
sorted(a)
[13, 76, 134, 433, 567]
len(a)
5
a
[567, 76, 13, 433, 134]
id(a)
2324487833344
a[0]
567
a[0]
567
a
[567, 76, 13, 433, 134]
id(a)
2324487833344
a[3]=43

a
[567, 76, 13, 43, 134]
id[a]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    id[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
id(a)
2324487833344
a.append(55)
a
[567, 76, 13, 43, 134, 55]
a.append(60)
a
[567, 76, 13, 43, 134, 55, 60]
a.insert(1,65)
a
[567, 65, 76, 13, 43, 134, 55, 60]
a.extend([1,2,3,4,5])
a
[567, 65, 76, 13, 43, 134, 55, 60, 1, 2, 3, 4, 5]
a
[567, 65, 76, 13, 43, 134, 55, 60, 1, 2, 3, 4, 5]
a.pop()
5
a
[567, 65, 76, 13, 43, 134, 55, 60, 1, 2, 3, 4]
a.pop(0)
567
a.pop(6)
60
a.pop(11)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.pop(11)
IndexError: pop index out of range
a.pop(11)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.pop(11)
IndexError: pop index out of range
a.remove(23)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.remove(23)
ValueError: list.remove(x): x not in list
a.remove(43)
a
[65, 76, 13, 134, 55, 1, 2, 3, 4]
del a[1]
a
[65, 13, 134, 55, 1, 2, 3, 4]
del a[5]
a
[65, 13, 134, 55, 1, 3, 4]
a.clear()
a
[]
id(a)
2324487833344
a = [66,13,50,60,14,11]
a.index(13)
1
a
[66, 13, 50, 60, 14, 11]
a.count(50)
1
a = [1,2,3,4]
>>> b = a
>>> b
[1, 2, 3, 4]
>>> b.append(7)
>>> a
[1, 2, 3, 4, 7]
>>> b
[1, 2, 3, 4, 7]
>>> c = a.copy()
>>> a
[1, 2, 3, 4, 7]
>>> c = a.copy
>>> c.append
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    c.append
AttributeError: 'builtin_function_or_method' object has no attribute 'append'
>>> c.append(12)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    c.append(12)
AttributeError: 'builtin_function_or_method' object has no attribute 'append'
>>> c = a.copy
>>> c.append(12)
... 
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    c.append(12)
AttributeError: 'builtin_function_or_method' object has no attribute 'append'
>>> c
<built-in method copy of list object at 0x0000021D38CDA400>
>>> c = a.copy
... c.append(12)
... 
... c
SyntaxError: multiple statements found while compiling a single statement
>>> c = a.copy()
... c.append(12)
... c
SyntaxError: multiple statements found while compiling a single statement
>>> c = a.copy
... c.append(12)
... a
SyntaxError: multiple statements found while compiling a single statement
>>> c
<built-in method copy of list object at 0x0000021D38CDA400>
