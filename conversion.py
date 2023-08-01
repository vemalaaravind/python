Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#type conversion
num=2
type(num)
<class 'int'>
type(2.2)
<class 'float'>
add =321+234
add
555
62*2.4
148.79999999999998
2**3
8
import math
math.pi
3.141592653589793
import random
random.random()
0.0791748514803543
# string objects in python
a = "india"
print(a)
india
a[0]
'i'
a[-1]
'a'
a[1:]
'ndia'
a[:-1]
'indi'
print(a+ 'xyz')
indiaxyz
a*7
'indiaindiaindiaindiaindiaindiaindia'
a.replace('ia','xyz')
'indxyz'
#list objects in python
l1 = [101,'america',2.05]
len(l1)
3
l1[1]
'america'
l1[;-1]
SyntaxError: invalid syntax
l1[:-1]
[101, 'america']
l1.append('usa')
print(l1)
[101, 'america', 2.05, 'usa']
l1.pop(3)
'usa'
l1.pop(0)
101
l1.reverse()
print(l1)
[2.05, 'america']
l1.push(3)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l1.push(3)
AttributeError: 'list' object has no attribute 'push'
l.push('america)
       
SyntaxError: incomplete input
l1.push('america')
       
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l1.push('america')
AttributeError: 'list' object has no attribute 'push'
#dictionary
       
dict1 = {1:'Tiger',2:'wolf',3:'mouse'}
       
print(dict1)
       
{1: 'Tiger', 2: 'wolf', 3: 'mouse'}
dict1.keys()
       
dict_keys([1, 2, 3])
dict1.values()
       
dict_values(['Tiger', 'wolf', 'mouse'])
dict1[4]
       
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    dict1[4]
KeyError: 4
>>> dict1[4]='cat'
...        
>>> print(dict1)
...        
{1: 'Tiger', 2: 'wolf', 3: 'mouse', 4: 'cat'}
>>> #tuple objects
...        
>>> T1=(1,2,3,4)
...        
>>> len(T1)
...        
4
>>> T2=T1+(7,9)
...        
>>> print(T2)
...        
(1, 2, 3, 4, 7, 9)
>>> T2[3]
...        
4
>>> #file objects
...        
>>> f1=open('C:/Users/Aravind/OneDrive/Desktop/data.txt','w')
...        
>>> f1.write('hi,This is aravind\n)
...          
SyntaxError: incomplete input
>>> f1.write(' Hii,my dear PC This is ur boss global star\n')
...          
44
>>> f1.write('Ram charan is konown as global star waiting for Game Changer\n')
...          
61
>>> fl.close()
...          
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    fl.close()
NameError: name 'fl' is not defined. Did you mean: 'f1'?
>>> f1.write('hello my dear pc')
...          
16
f1.close()
         
#sets
         
s=set('INDia')
         
s1=set(['u','s','a'])
         
print(s,s1)
         
{'D', 'i', 'a', 'N', 'I'} {'u', 'a', 's'}
print(s&s1)
         
{'a'}
\
s|s1
         
{'I', 'N', 'D', 'u', 'i', 'a', 's'}
s-s1
         
{'I', 'N', 'i', 'D'}
a=7
         
b=2.2
         
r=a=
         
SyntaxError: incomplete input
r=a+b
         
print(r)
         
9.2
type(r)
         
<class 'float'>
#it is an impliciat type conversion if we add an integer with floating value it produces an floating value
         
a=7
         
b=9
         
e=a+b
         
print(e)
         
16
type(e)
         
<class 'int'>
a=8
         
b=9.0
         
e=a+b
         
print(e)
         
17.0
e=int(a+b)
         
type(e)
         
<class 'int'>
#string and int addition
         
a = 7
         
b = '2'
         
r = a + b
         
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    r = a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
r=a+b
         
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    r=a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
 a = 7
         
SyntaxError: unexpected indent
a=9
         
b='2'
         
r=a+int(b)
         
print(r)
         
11
a = 77.9
         
int_a=int(a)
         
type(int_a)
         
<class 'int'>
a=50
         
float_a=float(a)
         
type(float_(a))
         
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    type(float_(a))
NameError: name 'float_' is not defined. Did you mean: 'float_a'?
type(float_a)
         
<class 'float'>
a=50
         
comp_a=complex(a)
         
print(comp_a)
         
(50+0j)
a=50
         
str
         
<class 'str'>
-
a=50
         
str_a=str(a)
         
str_a
         
'50'
type(str_a)
         
<class 'str'>
s="INDIA"
         
ts=tuple(s)
         
print(ts)
         
('I', 'N', 'D', 'I', 'A')
s="INDIA"
         
l1=list(s)
         
print(l1)
         
['I', 'N', 'D', 'I', 'A']
typw(l1)
         
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    typw(l1)
NameError: name 'typw' is not defined. Did you mean: 'type'?
'
type(l1)
         
<class 'list'>
type(ts)
         
<class 'tuple'>
t=("tommy","aravind","markwood")
         
l2=list(t)
         
print(l2)
         
['tommy', 'aravind', 'markwood']
type(l2)
         
<class 'list'>
a=10
         
b=bin(a)
         
c=hex(a)
         
print(c)
         
0xa
b=oct(b)
         
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    b=oct(b)
TypeError: 'str' object cannot be interpreted as an integer
print(b)
         
0b1010
#converting number to corresponding ASCII character
         
n1=76
         
chr(n1)
         
'L'
n2=90
         
chr(n2)
         
'Z'
#convert string into unqiue code value
         
s='A'
         
r=ord(s)
         
print(r)
         
65
