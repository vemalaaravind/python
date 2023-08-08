Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list1=[1,'adam',102,'USA']#the lists are ordere
#2list can store various typeof elements
#3list allow duplicate values
l1=['apple' 'orange' 'spoata' 'kiwi']
print(l1)
['appleorangespoatakiwi']
l2=['apple',[8,4,6], 'bananna','orange']
print(l2)
['apple', [8, 4, 6], 'bananna', 'orange']
print(l1[2])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(l1[2])
IndexError: list index out of range
print(l1[2])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(l1[2])
IndexError: list index out of range
 print(l2[2])
 
SyntaxError: unexpected indent
print(l2[2])
bananna
prin(list[-1])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    prin(list[-1])
NameError: name 'prin' is not defined. Did you mean: 'print'?
print(l2[-1]))
SyntaxError: unmatched ')'
print(l2[-1])
orange
print(l2(1:)]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print(l2[1:])
[[8, 4, 6], 'bananna', 'orange']
l2.extend(['water melon', 'musk melon,])
           
SyntaxError: incomplete input
l2.extend(['water melon', 'musk melon',])
           
print(l2)
           
['apple', [8, 4, 6], 'bananna', 'orange', 'water melon', 'musk melon']
l2.remove('orange')
           
print(l2)
           
['apple', [8, 4, 6], 'bananna', 'water melon', 'musk melon']
print(list1.pop(1))
           
adam
list1.clear()
           
print(list1)
           
[]
list1.reverse()
           
print(list1)
           
[]
l2.reverse()
           
print9l2)
          
SyntaxError: unmatched ')'
print(l2)
          
['musk melon', 'water melon', 'bananna', [8, 4, 6], 'apple']
print(l2.count('musk melon'))
          
1
#tuples
          
#tuples are ordered
          
#we can access by index
          
#unchangable
          
#they can store various datatypes
          
tup1=('apple', 'orange', 'banana', 'kiwi')
          
print(type(tup1))
          
<class 'tuple'>
tup2=('apple')
          
print(tup2)
          
apple
print(tup1[0])
          
apple
print(tup1[-1])
          
kiwi
print(tup1[1:3]))
SyntaxError: unmatched ')'
print(tup1[1:3])
('orange', 'banana')
print(("repeat",)*3)
('repeat', 'repeat', 'repeat')
print(tup1.index('banana'))
2
>>> y=list(tup1)
>>> y.append('guava')
>>> tup1=tuple(y)
>>> print(tup1)
('apple', 'orange', 'banana', 'kiwi', 'guava')
>>> tup3=('cherry',)
>>> tup+=tup3
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    tup+=tup3
NameError: name 'tup' is not defined. Did you mean: 'tup1'?
>>> tup1+=tup3
>>> print(tup1)
('apple', 'orange', 'banana', 'kiwi', 'guava', 'cherry')
>>> for x in tup1:
...     print(x)
... 
...     
apple
orange
banana
kiwi
guava
cherry

>>> 
>>> #Dictionaries
>>> dict1 = {1:'apple',2:'orange',3:'banana',4:'kiwi'}
>>> print(dict1)
{1: 'apple', 2: 'orange', 3: 'banana', 4: 'kiwi'}
>>> print(dict1[1])
apple
>>> print(dict1[1:])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(dict1[1:])
TypeError: unhashable type: 'slice'
>>> print(dict1.get(1))
apple
>>> print(dict1.pop(4))
kiwi
>>> print(dict1)
{1: 'apple', 2: 'orange', 3: 'banana'}
>>> print(len(dict1))
3
>>> print(soted(dict1))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(soted(dict1))
NameError: name 'soted' is not defined. Did you mean: 'sorted'?
print(sorted(dict1))
[1, 2, 3]
print(dict1.keys())
dict_keys([1, 2, 3])
print(dict1.values())
dict_values(['apple', 'orange', 'banana'])
dict1.update({2:'watermelon',3:'banana'})
print(dict1)
{1: 'apple', 2: 'watermelon', 3: 'banana'}
dict.update({5:'muskmelon'})
print(dict1)
{1: 'apple', 2: 'watermelon', 3: 'banana'}
dict1.update({5:'muskmelon'})

print(dict1)
SyntaxError: multiple statements found while compiling a single statement
dict1.update({5:'muskmelon'})





dict1.update({5:'watermelon'})
prin(dict1)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    prin(dict1)
NameError: name 'prin' is not defined. Did you mean: 'print'?
print(dict1)
{1: 'apple', 2: 'watermelon', 3: 'banana', 5: 'watermelon'}
dict1.popitem()
(5, 'watermelon')
print(dict1)
{1: 'apple', 2: 'watermelon', 3: 'banana'}
for x in dict1:
    print(dict1[x])

    
apple
watermelon
banana
for x,y in dict1.items():
    print(x,y)

    
1 apple
2 watermelon
3 banana
mydict = dict1.copy()
print(mydict)
{1: 'apple', 2: 'watermelon', 3: 'banana'}
dict1.clear()
print(dict1)
{}
