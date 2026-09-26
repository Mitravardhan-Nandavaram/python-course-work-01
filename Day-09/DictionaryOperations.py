Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#mut ord het dyn unidu
d = {}
type(d)
<class 'dict'>
d = {1:4,2:8,3:13}
d
{1: 4, 2: 8, 3: 13}
d
{1: 4, 2: 8, 3: 13}
d = {}
d = []
d[1]=1
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d[1]=1
IndexError: list assignment index out of range
d = {}
d[1]=1
d[12.3]=1
d['str']=1
d[(1,2,4}]=1
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
d[(1,2,4)]=1
d[(2+3j)]=1
d[Yrue]=1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[Yrue]=1
NameError: name 'Yrue' is not defined. Did you mean: 'True'?
d[True]=1
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
d[False]=1
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1}
d[1]=1
d[2]=12.3
d[3]='str'
d[4]=2+3j
d[5]=True
d[6]=[1,2,3]
d[7]=(1,2,3)
d[8]={1,2,3}
d[9]=frozenset({1,2,3})
d[10]={1:1,2:2}
d[11]=None
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}
d={}
d[1]=3
d
{1: 3}
data
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data
NameError: name 'data' is not defined
data = {'name':'mitra','batch':'65','course'}
SyntaxError: ':' expected after dictionary key
data = {'name':'mitra','batch':'65','course':'pfs'}
data.get('name')
'mitra'
data.get('batch')
'65'
data.get('age')
data.get('age','key is not present')
'key is not present'
data.get('batch','key is not present')
'65'
data
{'name': 'mitra', 'batch': '65', 'course': 'pfs'}
data[age]=23
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    data[age]=23
NameError: name 'age' is not defined
data['age']=23
data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23}
data['phnno']=8498065355
data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355}
data.update({'email':'mithra@gmail.com','py':2026})
data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026}
id(data)
2124745457152
data['py']
2026
data['py']=2027
data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2027}
data['age']=22
id(data)
2124745457152
data.popitem()
('py', 2027)
data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 22, 'phnno': 8498065355, 'email': 'mithra@gmail.com'}
data.pop('course')
'pfs'
data
{'name': 'mitra', 'batch': '65', 'age': 22, 'phnno': 8498065355, 'email': 'mithra@gmail.com'}
data.pop('email')
'mithra@gmail.com'
data
{'name': 'mitra', 'batch': '65', 'age': 22, 'phnno': 8498065355}
del data['batch']
data
{'name': 'mitra', 'age': 22, 'phnno': 8498065355}
del data['age']
data
{'name': 'mitra', 'phnno': 8498065355}
data.clear()
data
{}
data
{}
data.key('name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026)
SyntaxError: invalid syntax
data = ('name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026)
SyntaxError: invalid syntax
data = ('name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2027)
SyntaxError: invalid syntax
data={'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026}
data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026}
len(data)
7
data.keys()
dict_keys(['name', 'batch', 'course', 'age', 'phnno', 'email', 'py'])
data.values()
dict_values(['mitra', '65', 'pfs', 23, 8498065355, 'mithra@gmail.com', 2026])
data.items()
dict_items([('name', 'mitra'), ('batch', '65'), ('course', 'pfs'), ('age', 23), ('phnno', 8498065355), ('email', 'mithra@gmail.com'), ('py', 2026)])
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phnno', 'py']
>>> min(data)
'age'
>>> max(data)
'py'
>>> len(data)
7
>>> d={1:1,2:2}
>>> m=d
>>> m
{1: 1, 2: 2}
>>> d
{1: 1, 2: 2}
>>> n=d.copy()
>>> n[5]=5
>>> n
{1: 1, 2: 2, 5: 5}
>>> d
{1: 1, 2: 2}
>>> data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026}
>>> data.get('py')
2026
>>> data.setdefault('py',2026)
2026
>>> data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026}
>>> data.setdefault('name',2026)
'mitra'
>>> data.setdefault('email',2026)
'mithra@gmail.com'
>>> data.setdefault('key',2026)
2026
>>> data
{'name': 'mitra', 'batch': '65', 'course': 'pfs', 'age': 23, 'phnno': 8498065355, 'email': 'mithra@gmail.com', 'py': 2026, 'key': 2026}
>>> dict.fromkeys(["python","mysql","java"],0)
{'python': 0, 'mysql': 0, 'java': 0}
