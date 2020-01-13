# 0x07. Python - Test-driven development

## 0-add_integer.py, tests/0-add_integer.txt
Function that adds 2 numbers.

- The two numbers must be integers or floats, otherwise raises a TypeError exception with the message a must be an integer or b must be an integer
- The two numbers are first casted to integers if they are float
- Returnsthe addition of the two numbers
- No extra modules imported

_Example:_

```
~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
~/0x07$
```

## 2-matrix_divided.py, tests/2-matrix_divided.txt
Function that divides all elements of a matrix.

- The matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
- The number the matrix is divided by must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
- The number the matrix is divided by can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
- All elements of the matrix will be divided and rounded to 2 decimal places
- Returns a new matrix
- No module imported

_Example:_

```
~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
~/0x07$
```

## 3-say_my_name.py, tests/3-say_my_name.txt
Function that prints My name is <first name> <last name>

- first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
- No module imported

_Example:_

```
~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
~/0x07$
```

## 4-print_square.py, tests/4-print_square.txt


## 5-text_indentation.py, tests/5-text_indentation.txt

## tests/6-max_integer_test.py
