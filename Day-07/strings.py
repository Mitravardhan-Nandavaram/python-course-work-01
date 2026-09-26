#strings operations
Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = '   hello world  '
s.strip()
'hello world'
s.1strip()
SyntaxError: invalid decimal literal
s.lstrip()
'hello world  '
s.rstrip()
'   hello world'
s.replace(' ','')
'helloworld'
s.replace(" ","")
'helloworld'
s='java-python-flask-mysql-fastapi-c'
s.split('-',2)
['java', 'python', 'flask-mysql-fastapi-c']
ls='java-python-flask-mysql-fastapi-c'
ls.split('-')
['java', 'python', 'flask', 'mysql', 'fastapi', 'c']
s.split('-',2)
['java', 'python', 'flask-mysql-fastapi-c']
l = '''python'''
l = '''python'''
java
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    java
NameError: name 'java' is not defined
l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c = ['python','java','mysql','flask']
c
['python', 'java', 'mysql', 'flask']
''.join(c)
'pythonjavamysqlflask'
' '.join(c)
'python java mysql flask'
', '.join(c)
'python, java, mysql, flask'
'@'.join(c)
'python@java@mysql@flask'
'-'.join({'1','2','3'})
'1-2-3'
'-'.join({'1','2','3'})
'1-2-3'
a = 'string.py'
a.partition('.')
('string', '.', 'py')
a = 'string.py.java.png.txt'
s
'java-python-flask-mysql-fastapi-c'
a
'string.py.java.png.txt'
a.parttion
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.parttion
AttributeError: 'str' object has no attribute 'parttion'. Did you mean: 'partition'?
a.parttion('.')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.parttion('.')
AttributeError: 'str' object has no attribute 'parttion'. Did you mean: 'partition'?
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
a.startswith('str')
True
a.startswith('list')
False
a.endwith('.py')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.endwith('.py')
AttributeError: 'str' object has no attribute 'endwith'. Did you mean: 'endswith'?
a.endswith('.py')
False
>>> a.endswith('.png')
False
>>> 'pythonv.13'.islower()
True
>>> 'pythonv.13'.islowere()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    'pythonv.13'.islowere()
AttributeError: 'str' object has no attribute 'islowere'. Did you mean: 'islower'?
>>> 
... 'pythonv.13'.islower()
True
>>> 'PYTHON243567@#$%'.isupper()
True
>>> 'estyu'.isalpha()
True
>>> 'estyu8765@'.isalpha()
False
>>> 'serdtfyguhjok'.isalnum()
True
>>> '    '.isspace()
True
>>> '   Hello'.istitle()
True
>>> '   Hell0'.isspace
<built-in method isspace of str object at 0x00000218AE6E9870>
>>> 
... '   Hell0'.isspace()
False
>>> 'Hlo'.istitle()
True
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> a.partition('.')
('string', '.', 'py.java.png.txt')
>>> '1234567'.isdecimal()
True
>>> 'ERTYGVYU7544'.isdecimal()
False
>>> '44567'.isdigit()
True
>>> '7544'.isnumeric()
True
