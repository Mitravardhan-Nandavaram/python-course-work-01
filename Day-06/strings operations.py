#String operation
Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="codegnan"
s
'codegnan'
type(s)
<class 'str'>
s+ ''
'codegnan'
a = 'python'
b = 'programming'
a+b
'pythonprogramming'
fname = 'mitra'
lname = 'vardhan'
fname + lname
'mitravardhan'
a
'python'
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
'*'*20
'********************'
'-codegnan-'*5
'-codegnan--codegnan--codegnan--codegnan--codegnan-'
names ="mitra vardhan"
name[0:6]
name[7:14]
name[:6]
name[7:]
SyntaxError: multiple statements found while compiling a single statement
print(name[0:6])
print(name[7:14])
print(name[:6])
print(name[7:])
Output
SyntaxError: multiple statements found while compiling a single statement
print(name[0:6])
print(name[7:14])
print(name[:6])
print(name[7:])
SyntaxError: multiple statements found while compiling a single statement
name = "Mithra"

print(name[0])
print(name[1])
print(name[2])
print(name[5])
SyntaxError: multiple statements found while compiling a single statement
names = "mitra vardhan ranjith rasool"
names
'mitra vardhan ranjith rasool'
names[5]
' '
names[8]
'r'
names[9]
'd'
names[-4]
's'
names[-6]
'r'
name[:5]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name[:5]
NameError: name 'name' is not defined. Did you mean: 'fname'?
names[:5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
names[:5]
'mitra'
names[:8]
'mitra va'
names[-9]
't'
'vardhan' is not in names
SyntaxError: invalid syntax
'vardhan' in names
True
True
True
'vardhan' is not names
True
'teja' is not names
True
'teja' in names
False
names
'mitra vardhan ranjith rasool'
len(names)
28
ord('a)
    
SyntaxError: unterminated string literal (detected at line 1)
ord('a')
    
97
ord('v')
    
118
ord('A')
    
65
chr(10)
    
'\n'
sorted(names)
    
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'd', 'h', 'h', 'i', 'i', 'j', 'l', 'm', 'n', 'n', 'o', 'o', 'r', 'r', 'r', 'r', 's', 't', 't', 'v']
max(names)
    
'v'
min(names)
    
' '
s = 'python programming language'
    
s.upper()
    
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
    
'python programming language'
s.capitalize()
    
'Python programming language'
s.swapcase
    
<built-in method swapcase of str object at 0x000001699370E830>
KeyboardInterrupt
s.swapcase()
    
'PYTHON PROGRAMMING LANGUAGE'
s.title()
    
'Python Programming Language'
s.casefold()
    
'python programming language'
s
    
'python programming language'
s.center(50,'*')
    
'***********python programming language************'
s.center(40,'.')
    
'......python programming language.......'
s.ljust(40,'.')
    
'python programming language.............'
s.rjust(40,'.')
    
'.............python programming language'
'123'.zfill(5)
    
'00123'
'123'.zfill(4)
    
'0123'
'545'z.fill(4)
    
SyntaxError: invalid syntax

'545'.zfill(4)
    
'0545'
s
    
'python programming language'
s.find('python')
    
0
s.find('g')
    
10
s.find(a)
    
0
s,rfind()
    
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s,rfind()
NameError: name 'rfind' is not defined. Did you mean: 'round'?
s,rfind('a')
    
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s,rfind('a')
NameError: name 'rfind' is not defined. Did you mean: 'round'?
s.rfind(a)
    
0
s.rfind('g')
    
25
s.rfind('a)
        
SyntaxError: unterminated string literal (detected at line 1)
s.rfind('a')
        
24
s.find('z')
        
-1
s.index('a)
        
SyntaxError: unterminated string literal (detected at line 1)
s.find('a')
        
12
s.index('a;
        
SyntaxError: unterminated string literal (detected at line 1)

s.index('a')
        
12
s.count('a)
        
SyntaxError: unterminated string literal (detected at line 1)
s.count('a')
        
3
s.count('m')
        
2
s
        
'python programming language'
s.replace('0')
        
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.replace('0')
TypeError: replace() takes at least 2 positional arguments (1 given)
s.replace('0';'1')
        
SyntaxError: invalid syntax
)
s.replace('0','1')
        
SyntaxError: unmatched ')'
s.replace('m','2')
        
'python progra22ing language'
s.replace('python','java')
        
'java programming language'
>>> s.marketrans('aeiou','#@$&*')
...         
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.marketrans('aeiou','#@$&*')
AttributeError: 'str' object has no attribute 'marketrans'. Did you mean: 'maketrans'?
>>> 
... s.maketrans('aeiou','#@$&*')
...         
{97: 35, 101: 64, 105: 36, 111: 38, 117: 42}
>>> s.translate(s.maketrans('aeiou','#@$*'))
...         
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.translate(s.maketrans('aeiou','#@$*'))
ValueError: the first two maketrans arguments must have equal length
>>> 
... s.translate(s.maketrans('aeiou','#@$*'))
...         
Traceback (most recent call last):
  File "<pyshell#92>", line 2, in <module>
    s.translate(s.maketrans('aeiou','#@$*'))
ValueError: the first two maketrans arguments must have equal length
>>> }
... s.translate(s.maketrans('aeiou','#@$*'))
...         
... s.translate(s.maketrans('aeiou','#@$&*'))
...         
SyntaxError: unmatched '}'
>>> s.translate(s.maketrans('aeiou','#@$&*'))
...         
'pyth&n pr&gr#mm$ng l#ng*#g@'
>>> text="hello world"
...         
>>> text.encode()
...         
b'hello world'
>>> text="hello😊"
...         
>>> text.encode()
...         
b'hello\xf0\x9f\x98\x8a'
>>> b'Hello \xf0\x9f\x98\x8a'.decode()
...         
'Hello 😊'
