Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,3,5.67,"tuba","shah"]
l
[1, 2, 3, 5.67, 'tuba', 'shah']
type(l)
<class 'list'>
l[3]
5.67
l[4]
'tuba'
l[6]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l[6]
IndexError: list index out of range
l[1:5]
[2, 3, 5.67, 'tuba']
l[4:5]
['tuba']
l[:5]
[1, 2, 3, 5.67, 'tuba']
l[-1]
'shah'
l[-3:-1]
[5.67, 'tuba']
l[:0]
[]
l[::-1]
['shah', 'tuba', 5.67, 3, 2, 1]
l[:-1]
[1, 2, 3, 5.67, 'tuba']
l
[1, 2, 3, 5.67, 'tuba', 'shah']
l.append(200)
l
[1, 2, 3, 5.67, 'tuba', 'shah', 200]
l.extend(12,30)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.extend(12,30)
TypeError: list.extend() takes exactly one argument (2 given)
l[-2:0]
[]
l[-2:-1]
['shah']
l[::-2]
[200, 'tuba', 3, 1]
l[2:-2]
[3, 5.67, 'tuba']
l.extend([12,30])
l
[1, 2, 3, 5.67, 'tuba', 'shah', 200, 12, 30]
l.insert(2,34)
l
[1, 2, 34, 3, 5.67, 'tuba', 'shah', 200, 12, 30]
l.remove(34)
l
[1, 2, 3, 5.67, 'tuba', 'shah', 200, 12, 30]
l.pop(6)
200
l
[1, 2, 3, 5.67, 'tuba', 'shah', 12, 30]
[1, 2, 3, 5.67, 'tuba', 'shah', 12, 30]
[1, 2, 3, 5.67, 'tuba', 'shah', 12, 30]
l.index(30)
7
l.sort()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
l.count("tuba")
1
l.len()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l.len()
AttributeError: 'list' object has no attribute 'len'
len(l)
8
b=l.copy()
b
[1, 2, 3, 5.67, 'tuba', 'shah', 12, 30]
l
[1, 2, 3, 5.67, 'tuba', 'shah', 12, 30]
b.clear()
b
[]
l.reverse()
l
[30, 12, 'shah', 'tuba', 5.67, 3, 2, 1]
l.insert(-2,"ooh")
l
[30, 12, 'shah', 'tuba', 5.67, 3, 'ooh', 2, 1]
l.pop(-3)
'ooh'
l
[30, 12, 'shah', 'tuba', 5.67, 3, 2, 1]
l.reverse()
l
[1, 2, 3, 5.67, 'tuba', 'shah', 12, 30]
l.insert(-2,"ooh")
l
[1, 2, 3, 5.67, 'tuba', 'shah', 'ooh', 12, 30]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:
== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
[]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:1 2 3 4 5
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 8, in <module>
    i=int(input("Enter numbers:"))
ValueError: invalid literal for int() with base 10: '1 2 3 4 5'

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:1
Enter numbers:2
Enter numbers:3
Enter numbers:4
Enter numbers:5
[1, 2, 3, 4, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:
1
2
3
4
5
[1, 2, 3, 4, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 6, in <module>
    for i in range(n):
NameError: name 'n' is not defined

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
[1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
1
2
3
4
5
6

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 16, in <module>
    sum=sum+l[i]
TypeError: list indices must be integers or slices, not float

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 16, in <module>
    sum=sum+l[i]
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'float'

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 16, in <module>
    sum=sum+l[i]
TypeError: list indices must be integers or slices, not float

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 16, in <module>
    sum=sum+i
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'float'

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
sum is: 11.0 avg is: 2.75

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
1
2
3
4
5
0
1
2
3
4

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:
== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:
[]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:
[]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:
1
2
3
4
5
[1, 2, 3, 4, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:
1
2
3
4
5
[1, 2, 3, 4, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
size:5
Enter numbers:
1
2
3
4
5
[1, 2, 3, 4, 5]
[2, 4]
[1, 3, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:1 2 3 4 5
[1, 2, 3, 4, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:1 2 3 4 5
[1, 2, 3, 4, 5]
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 54, in <module>
    while i<len(l):
NameError: name 'i' is not defined. Did you mean: 'id'?

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:1 2 3 4 5
[1, 2, 3, 4, 5]
[2, 4]
[1, 3, 5]

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:1 2 3 4 5
Traceback (most recent call last):
  File "C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py", line 67, in <module>
    l=list(map(int,input("Enter numbers:")).split())
AttributeError: 'map' object has no attribute 'split'

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:1 2 3 4 5
[1, 2, 3, 4, 5]
sum is: <built-in function sum>

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:1 2 3 4 5
[1, 2, 3, 4, 5]
sum is: 15

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:12 23 45 67
[12, 23, 45, 67]
product is: 832140

== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
Enter numbers:100 20 3 4
[100, 20, 3, 4]
product is: 24000
l=elements for elements in "Good Afternoon"
SyntaxError: invalid syntax
l=[elements for elements in "Good Afternoon"]
l
['G', 'o', 'o', 'd', ' ', 'A', 'f', 't', 'e', 'r', 'n', 'o', 'o', 'n']
s=
SyntaxError: incomplete input
s={1,2.3,6}
s
{1, 2.3, 6}
>>> type(s)
<class 'set'>
>>> s={1,2,3,3,2,2}
>>> s
{1, 2, 3}
>>> 
== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
['hello', 'hii']
>>> 
== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
[4, 8, 16, 32, 64, 128, 256, 512]
>>> 
== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
[100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
>>> 
== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
[4, 16, 64, 256]
>>> s1={1,2,3}
>>> s2{1,2,3,4}
SyntaxError: invalid syntax
>>> s1.issuperset(s2)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s1.issuperset(s2)
NameError: name 's2' is not defined. Did you mean: 'l2'?
>>> s2={1,2,3,4}
>>> s1={1,2,3}
>>> s1.issuperset(s2)
False
>>> 
== RESTART: C:/Users/Shah/OneDrive/Desktop/DAY_3_WKSP/Day_3_exercise_progs.py ==
[1, 2, 3, 4]
>>> s1={1,2,3}
>>> s2={5,6,7}
>>> s1^s2
{1, 2, 3, 5, 6, 7}
>>> s1.add(33)
>>> s1
{1, 2, 3, 33}
