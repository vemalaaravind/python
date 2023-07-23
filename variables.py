Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======================== RESTART: D:/demo1.py =======================
Enter first number:10
Enter second number:23
addition of two numbers=c
>>> a=int(input("Enter first number:"))
Enter first number:10
>>> b=int(input("Enter second number:"))
Enter second number:34
>>> c=a+b
>>> print(c)
44
>>> 
======================== RESTART: D:/demo1.py =======================
Enter first number:23
Enter second number:33
56
>>> c=a*b
>>> print(c)
759
>>> d=a/b
>>> print(d)
0.696969696969697
>>>   // car = "BMW"
...   
SyntaxError: unexpected indent
>>> a = 52
>>> print(a)
52
>>> type(a)
<class 'int'>
>>> id(a)
140709105035656
>>>  # id fucntion is used to specified an object by unique identification
...  
>>> a=100
>>> id(a)
140709105037192
>>> (x,y,,z)= 50,12,13.35
SyntaxError: invalid syntax
>>> (x,y,z)=50,13.5,"Aravind"
>>> type(y)
<class 'float'>
>>> type(z)
<class 'str'>
id(z)
2710562343280
#multiple variables in single line

# there is a another wat to assign multiple variables in a single line
p=i=o=10
prinr(p)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    prinr(p)
NameError: name 'prinr' is not defined. Did you mean: 'print'?
print(p)
10
print(p,i,o)
10 10 10
id(p,i,o)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    id(p,i,o)
TypeError: id() takes exactly one argument (3 given)
id(o)
140709105034312
a102="ANDHRA"
print(a102)
ANDHRA
-dog="rhyme"
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

_dog="rhyme"
print(_dog)
rhyme
name_age="aravind 20"
print(name_age)
aravind 20
#variable name should not be start with a number what happen if we write lets see
1name="virat"
SyntaxError: invalid decimal literal
@age = 40
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
name$= 40
SyntaxError: invalid syntax

car = "BMW"
print(car)
BMW
Car = "Tata"
print(Car)
Tata
print(car)
BMW
CAR = "volvo"
print(CAR)
volvo
break = 60
SyntaxError: invalid syntax
for =90
SyntaxError: invalid syntax
#keywords cannot be used as variables
#operartions performed on python vcariables
a=343
b=908
result=a+b
print(result)
1251
result=a-b
print(result)
-565
result=a/b
print(result)
0.3777533039647577
country = 'India'
print(country)
India
contry[3]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    contry[3]
NameError: name 'contry' is not defined. Did you mean: 'country'?
country[4]
'a'
country[:3]
'Ind'
country[1:]
'ndia'
 cars = ["volovo,innova,fortuner,breeza)
         
SyntaxError: unexpected indent
cars = ["volovo,innova,fortuner,breeza)
        
SyntaxError: incomplete input
cars = ["volovo","innova","fortuner","breeza")
        
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
cars = ["volovo","innova","fortuner","breeza"]
        
print(cars)
        
['volovo', 'innova', 'fortuner', 'breeza']
['volovo', 'innova', 'fortuner', 'breeza']
        
['volovo', 'innova', 'fortuner', 'breeza']
p,o,i,u
        
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    p,o,i,u
NameError: name 'u' is not defined
p,o,i,u=cars
        
print(u)
        
breeza
print(u,i,o,p)
        
breeza fortuner innova volovo
x = "Aravind"
        
print("welcome to " + x)
        
welcome to Aravind
# we cannot add integer to a string
        
x=90
        
y="khkdjslhfijfdlk"
        
print(x+y)
        
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
x=20
        
my Department = "Marketing"
        
SyntaxError: invalid syntax
myDepartment = "Marketing
        
SyntaxError: incomplete input
myDepartment = "Information Technology"
        
print(myDepartment)
        
Information Technology
carBrand = "wolksowogan"
        
print(carBrand)
        
wolksowogan
My Name = "Aravind"
        
SyntaxError: invalid syntax
MyName="Aravind"
        
print(MyName)
        
Aravind
#snake case
        
citty_address="delhi"
        
print(city_adress)
        
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(city_adress)
NameError: name 'city_adress' is not defined. Did you mean: 'citty_address'?
print(city_address)
        
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print(city_address)
NameError: name 'city_address' is not defined. Did you mean: 'citty_address'?
print(citty_address)
        
delhi
city_adress="visakapatnam-gajuwaka"
        
print(city_adress)
        
visakapatnam-gajuwaka
