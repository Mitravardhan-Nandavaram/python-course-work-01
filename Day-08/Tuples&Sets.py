#Tuples in Python
Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    t
NameError: name 't' is not defined
t = ()
t = tuple()
t = (1,2,3,45)
t
(1, 2, 3, 45)
t = (1)
t
1
t =(1,)
t
SyntaxError: multiple statements found while compiling a single statement
t = (1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},(True)
t
     
SyntaxError: '(' was never closed
t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
     
t
     
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
type(t)
     
<class 'tuple'>
(1,2,3)+(4,5,6)
     
(1, 2, 3, 4, 5, 6)
t
     
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
     
23.4
t[-1]
     
True
t[-3]
     
{1, 2, 3}
t[2]
     
'str'
t[3:7]
     
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t
     
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
23.4 in t
     
True
'str' in t
     
True
true in t
     
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    true in t
NameError: name 'true' is not defined. Did you mean: 'True'?
False in t
     
False
True in t
     
True
t[-1:2,-2:1]
     
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t[-1:2,-2:1]
TypeError: tuple indices must be integers or slices, not tuple
t=(1,2,4,5,66,32,453,123,7898,1321,32)
     
t
     
(1, 2, 4, 5, 66, 32, 453, 123, 7898, 1321, 32)
sorted(t)
     
[1, 2, 4, 5, 32, 32, 66, 123, 453, 1321, 7898]
max(t)
     
7898
min(t)
     
1
len(t)
     
11
t
     
(1, 2, 4, 5, 66, 32, 453, 123, 7898, 1321, 32)
t.inde(32)
     
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t.inde(32)
AttributeError: 'tuple' object has no attribute 'inde'. Did you mean: 'index'?
t.index(32)
     
5
t.count(32)
     
2
all((1,2,3))
     
True
any((1,2,3,00,0))
     
True
all((1,2,3,00,0))
     
False
t = 1,2,3
     
t
     
(1, 2, 3)
a,b,c = t
     
a
     
1
b
     
2
c
     
3
t
     
(1, 2, 3)
t(1,2,3,4,[1,2,3],5)
     
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    t(1,2,3,4,[1,2,3],5)
TypeError: 'tuple' object is not callable
t=(1,2,3,4,[1,2,3],5)
     
t
     
(1, 2, 3, 4, [1, 2, 3], 5)
t[4]
     
[1, 2, 3]
t[4].append(5)
     
t
     
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t
     
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t=(1,2,34,4)
     
sum(t)
     
41
#SET mu unorder uni dyn he
     
s ={}
     
type(s)
     
<class 'dict'>
s = set()
     
s ={1,2,3,4,5,6134124,124,23345234,312}
     
s
     
{1, 2, 3, 4, 5, 6134124, 23345234, 312, 124}
s = {1,1,1,1,1,}
     
s
     
{1}
s = set()
     
s.add(1)
     
s.add(12.3)
     
s.add("str")
     
s.add(false)
     
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s.add(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
s.add(False)
     
s
     
{False, 1, 12.3, 'str'}
a = {1,2,3,4,5}
     
b = {3,5,7,8,9}
     
2 in a
     
True
10 not in a
     
True
a | b
     
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
     
{3, 5}
a - b
     
{1, 2, 4}
b - a
     
{8, 9, 7}
a ^ b
     
{1, 2, 4, 7, 8, 9}
a
     
{1, 2, 3, 4, 5}
#{1}{1,2},{1,2,3,5},{1,2,3,4,5},{4,5},{4,5,6}
     
a
     
{1, 2, 3, 4, 5}
{1}<=a
     
True
{1,2,3}
     
{1, 2, 3}
{1,7,8,9}<=a
     
False
a>={1,2}
     
True
a>={15,16}
     
False
m={1,2,3}
     
n={4,5,6}
     
n.isdisjoint(m)
     
True
a.isdisjoint(b)
     
False
a = {1,2,3,,4,5}
     
SyntaxError: invalid syntax
a = {1,2,3,4,5}
     
a
     
{1, 2, 3, 4, 5}
a ={12,43,1,7,89,40,23,44}
     
a
     
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
     
[1, 7, 12, 23, 40, 43, 44, 89]
min(a)
     
1
max(a)
     
89
all({1,1,23,43,13,1})
     
True
any({0,10})
     
True
a
     
{1, 7, 40, 43, 12, 44, 23, 89}
a = {1,2,3}
     
b = a
     
b.add(4)
     
a
     
{1, 2, 3, 4}
c.add(5)
     
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    c.add(5)
AttributeError: 'int' object has no attribute 'add'
a
     
{1, 2, 3, 4}
b
     
{1, 2, 3, 4}
c = a.copy
     
a
     
{1, 2, 3, 4}
a.add(5)
     
a
     
{1, 2, 3, 4, 5}
a.add(100)
     
a
     
{1, 2, 3, 4, 5, 100}
a.add(40)
     
a
     
{1, 2, 3, 4, 5, 100, 40}
a.add(101)
     
a
     
{1, 2, 3, 4, 5, 100, 101, 40}
a.
     
SyntaxError: invalid syntax
a.add({10,20,30,40})
     
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a.add({10,20,30,40})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
a.update({10,20,30,40})
...      
>>> a
...      
{1, 2, 3, 4, 5, 100, 101, 40, 10, 20, 30}
>>> a
...      
{1, 2, 3, 4, 5, 100, 101, 40, 10, 20, 30}
>>> a.pop()
...      
1
>>> a.pop()
...      
2
>>> a
...      
{3, 4, 5, 100, 101, 40, 10, 20, 30}
>>> a.remove(101)
...      
>>> a
...      
{3, 4, 5, 100, 40, 10, 20, 30}
>>> a
...      
{3, 4, 5, 100, 40, 10, 20, 30}
>>> a.discard(100)
...      
>>> a.discard(30)
...      
>>> a
...      
{3, 4, 5, 40, 10, 20}
>>> a.discard(30)
...      
>>> a
...      
{3, 4, 5, 40, 10, 20}
>>> a.clear()
...      
>>> a
...      
set()
>>> a = frozenset({1,2,3,4})
...      
>>> a
...      
frozenset({1, 2, 3, 4})
