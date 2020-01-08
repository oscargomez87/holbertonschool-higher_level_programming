# Project 0x05. Python - Exceptions

Understanding of error handling in python.

## 0-safe_print_list.py
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

## 1-safe_print_integer.py
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

## 2-safe_print_list_integers.py
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

## 3-safe_print_division.py
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

## 4-list_division.py
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

## 5-raise_exception.py
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

## 6-raise_exception_msg.py
Function that raises a name exception with a message.

- No modules imported.

_Example:_

```
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

## 100-safe_print_integer_err.py
Function that prints an integer.

- The integer _value_ can be any type (integer, string, etc.).
- The integer will be printed followed by a new line.
- Returns _True_ if the _value_ has been correctly printed (it means the _value_ is an integer).
- Otherwise, returns _False_ and prints in _stderr_ the error precede by _Exception:_.
- _try: / except:_ used.
- _"{:d}".format()_ is used to format the result.
- _type()_ not used.

_Example:_

```
~/0x05$ cat 100-main.py
#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

~/0x05$ ./100-main.py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
Holberton is not an integer
~/0x05$ ./100-main.py 2> /dev/null
89
-89
Holberton is not an integer
~/0x05$
```

## 101-safe_function.py
Function that executes a function safely.

- The function must be always a pointer to a function
- Returns the result of the function, otherwise returns _None_ if something happens during the function and prints in stderr the error precede by _Exception:_.
- _try: / except:_ used.

_Example:_

```
~/0x05$ cat 101-main.py
#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

~/0x05$ ./101-main.py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
~/0x05$ ./101-main.py 2> /dev/null
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None
~/0x05$
```

## 102-magic_calculation.py
function that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
