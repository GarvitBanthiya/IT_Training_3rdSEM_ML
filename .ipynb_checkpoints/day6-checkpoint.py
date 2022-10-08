Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def third(x):
    print('namaste')

    
third('abc')
namaste
def fourth(x):
    return x*10

fourth(5)
50
def fourth(x):
    print('hii')
    return x**2
    print('namaste')
    print('duniya')

    
fourth(3)
hii
9
def five(x,y,z):
    return(4,3,2)

five(4,3,2)def five(x,y,z):
    return(4,3,2)
SyntaxError: invalid syntax
def five(x,y,z:)
SyntaxError: invalid syntax
def five(x,y,z):
    return x+y+z

five(4,3,2)
9
def five(x,y,z):
    return x+y+z

six(3,4,5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    six(3,4,5)
NameError: name 'six' is not defined
five(3,4,5)
12
five(y=5,x=4,z=8)
17
def seven(x=1,y=3,z=23):
    return z-x-y

seven()
19
def eight(*x):
    return x

eight()
()
eight(2)
(2,)
eight(2,3,4)
(2, 3, 4)
eight(abc,cv)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    eight(abc,cv)
NameError: name 'abc' is not defined. Did you mean: 'abs'?
eight(34,avvbx)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    eight(34,avvbx)
NameError: name 'avvbx' is not defined
eight(23,34)
(23, 34)
eight(23,34,'khgvkh')
(23, 34, 'khgvkh')
def nine(**x)
SyntaxError: expected ':'
def nine(**x):
    return x

nine()
{}
nine(name='garvit',ph_no='8209939823')
{'name': 'garvit', 'ph_no': '8209939823'}
nine(n1=0,n2={5557,533,68},n3=['fcas','dfsd'])
{'n1': 0, 'n2': {68, 533, 5557}, 'n3': ['fcas', 'dfsd']}
def birthday
SyntaxError: invalid syntax
def birthday('garvit'):
    
SyntaxError: invalid syntax
def birthday('happy birthday' name):
    return name
SyntaxError: invalid syntax
def birthday(name):
    return 'happy birthday' name
SyntaxError: invalid syntax
def birthday(name):
    return name

def birthday(x):
    print('happy birthday ji')
    print('party kaha hai')
    print('{x}')
    return x

birthday(garvit)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    birthday(garvit)
NameError: name 'garvit' is not defined
def birthday(x):
    print('happy birthday ji')
    print('party kaha hai')
    print('{x}')

birthday('garvit')
happy birthday ji
party kaha hai
{x}
def birthday(x):
    print('happy birthday ji')
    print('party kaha hai')
    print('{x}')

    
birthday('d')
happy birthday ji
party kaha hai
{x}
def birthday(name):
    print('happy birthday ji')
    print('party kaha hai')
    print({name})

    
birthday('garvit')
happy birthday ji
party kaha hai
{'garvit'}
def birthday(name):
    print('happy birthday ji')
    print('party kaha hai')
    print(name)

    
birthday('garvit')
happy birthday ji
party kaha hai
garvit
def myfun(x,y,z)
SyntaxError: expected ':'
def myfun(x,y,z):
    return x+y+z

myfun(3,4,4)
11
myadd= Lambda x,y,z:
    
SyntaxError: invalid syntax
myadd= lambda x,y,z: x+y+z
myadd(5,5,5)
15
import math
math.pi
3.141592653589793
math.sqrt(64)
8.0
math.pow(2,3)
8.0
math.factorial(45)
119622220865480194561963161495657715064383733760000000000
math.factorial(09)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
math.factorial(9)
362880
import calender
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
import math
import calender
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
import datetime as dt
import calender
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

print(calendar.calendar.month(2022,9))
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print(calendar.calendar.month(2022,9))
AttributeError: 'function' object has no attribute 'month'
>>> print(calendar.month(2022,9))
   September 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30

>>> print(calendar.month(2023,5))
      May 2023
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

