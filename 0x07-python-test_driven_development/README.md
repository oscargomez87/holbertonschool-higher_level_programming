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

## 3-say_my_name.py, tests/3-say_my_name.txt

## 4-print_square.py, tests/4-print_square.txt

## 5-text_indentation.py, tests/5-text_indentation.txt

## tests/6-max_integer_test.py
