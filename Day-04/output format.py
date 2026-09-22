Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(a,b,c)
NameError: name 'a' is not defined
>>> a=10
>>> b=12.3
>>> c=codegnan
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c=codegnan
NameError: name 'codegnan' is not defined
>>> a=10
>>> b=12.5
>>> c='codegnan'
>>> print(a,b,c)
10 12.5 codegnan
>>> print("a=",a,"b=",b,'c=',c)
a= 10 b= 12.5 c= codegnan
>>> print("a=",a,"b",b,'c=',c,sep='')
a=10b12.5c=codegnan
>>> print("a=",a,"b",b,'c=',c,sep='\n')
a=
10
b
12.5
c=
codegnan
>>> print("a=",a,"b",b,'c=',c,sep='\t')
a=	10	b	12.5	c=	codegnan
>>> print("a=",a,"b",b,'c',c,sep='\t',end='\n\n')
a=	10	b	12.5	c	codegnan

>>> print("a=",a,"b",b,'c',c,sep='\t',end='@')
a=	10	b	12.5	c	codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.5 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.500000 c=codegnan
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.5 c=codegnan
>>> print('a={0} b={1} c={2}'.format(b,c,a))
a=12.5 b=codegnan c=10
>>> print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=12.5 c=codegnan
>>> print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=12.5 c=codegnan
