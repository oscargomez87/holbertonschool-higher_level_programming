# Project 0x05. Python - Exceptions

Understanding of error handling in python.

##0-safe_print_list.py##
Function that prints _x_ elements of a list.

- The list can contain any type (integer, string, etc.).
- All elements will be printed on the same line followed by a new line..
- x represents the number of elements to print.
- x can be bigger than the length of the list.
- Returns the real number of elements printed.
- No modules imported.
- _len()_ was not used.

_Example:_

```
~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
~/0x05$
```

##1-safe_print_integer.py##
Function that prints an integer with _"{:d}".format()_.

- The value received can be any type (integer, string, etc.).
- The integer will be printed followed by a new line.
- Returns True if value has been correctly printed (it means the value is an integer).
- Otherwise, returns False.
- _try: / except:_ used.
- _"{:d}".format()_ is used to format the output as integer
- No modules imported.
- _type()_ was not used.

_Example:_

```
~/0x05$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

~/0x05$ ./1-main.py
89
-89
Holberton is not an integer
~/0x05$
```

##2-safe_print_list_integers.py##
Function that prints the first _x_ elements of a list and only integers.

- The list can contain any type (integer, string, etc.)
- All integers will be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in the list
- x can be bigger than the length of the list - if it’s the case, an exception will occur
- Returns the real number of integers printed
- _try: / except:_ used.
- _"{:d}".format()_ is used to format the output as integer
- No modules imported.
- _len()_ was not used.

_Example:_

```
~/0x05$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "Holberton", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
~/0x05$
```

##3-safe_print_division.py##
Function that divides 2 integers and prints the result.

- The 2 values must always be integers
- The result of the division will be printed on the _finally:_ section preceded by _Inside result:_
- Returns the value of the division, otherwise: None
- _try: / except: / finally:_ used.
- _"{}".format()_ is used to format the result
- No modules imported.

_Example:_

```
~/0x05$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
~/0x05$
```

##4-list_division.py##
Function that divides element by element from 2 lists by a given length.

- The two lists can contain any type (integer, string, etc.)
- The given length can be bigger than the length of both lists
- Returns a new list (length = _list_length_) with all divisions
- If 2 elements can’t be divided, the division result will be equal to 0
- If an element is not an integer or float:
     - print: _wrong type_
- If the division can’t be done (/0):
     - print: _division by 0_
- If one of the two lists is too short
     - print: _out of range_
- _try: / except: / finally:_ used.
- No modules imported.

_Example:_

```
~/0x05$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

~/0x05$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
~/0x05$
```

##5-raise_exception.py##
Function that raises a type exception.

- No modules imported.

_Example:_

```
~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

~/0x05$ ./5-main.py
Exception raised
~/0x05$
```

##6-raise_exception_msg.py##
Function that raises a name exception with a message.

- No modules imported.

_Example:_

````
~/0x05$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

~/0x05$ ./6-main.py
C is fun
~/0x05$
```
