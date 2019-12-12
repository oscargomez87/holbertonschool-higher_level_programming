# 0x02-python-import_modules

* ***0-add.py***: imports the function __def add(a, b):__ from the file __add_0.p__ y and prints the result of the addition __1 + 2 = 3__.
  * **print()** function with string format used to display integers.
  * variables defined and assigned:
    * **a** with value **10**
    * **b** with value **5**
    * And used as arguments when calling the functions __add__ and __print__.
  * __a__ and __b__ are defined in 2 different lines: __a = 1__ and another __b = 2__.
  * Prints __<a value> + <b value> = <add(a, b) value>__ followed with a new line.
  * The word ADD_0 is used only once.
  *  __*__ or **\_\_import__** not used for importing.
  * Can't be executed when imported by using __\_\_import\_\_.
  *Example:*
  >$ cat add_0.py
  >#!/usr/bin/python3
  >def add(a, b):
  >"""My addition function
  >
  >Args:
  >a: first integer
  >b: second integer
  >
  >Returns:
  >The return value. a + b
  >"""
  >return (a + b)
  >
  >$ ./0-add.py
  >1 + 2 = 3
  >
  >$ cat 0-import_add.py
  >__import__("0-add")
  >$ python3 0-import_add.py
  >$

* ***1-calculation.py***: Imports functions from the file **calculator_1.py**, does some Maths, and prints the result.
  * **print()** function not used more than 4 times.
  * variables defined and assigned:
    * **a** with value **10**
    * **b** with value **5**
    * Only these variables will be used as arguemnts when calling functions (**print()** included).
  * **a** and **b** must be defined in 2 different lines: **a = 10** and another **b = 5**.
  * Calls each of the imported functions.
  * The word **calculator_1** is only used once.
  * __*__ or **\_\_import__** not used for importing.
  * Can't be executed when imported.
  *Example:*
  >$ cat calculator_1.py
  >#!/usr/bin/python3
  >def add(a, b):
  >    """My addition function
  >
  >    Args:
  >        a: first integer
  >        b: second integer
  >
  >    Returns:
  >        The return value. a + b
  >    """
  >    return (a + b)
  >
  >
  >def sub(a, b):
  >    """My subtraction function
  >
  >    Args:
  >        a: first integer
  >        b: second integer
  >
  >    Returns:
  >        The return value. a - b
  >    """
  >    return (a - b)
  >
  >
  >def mul(a, b):
  >    """My multiplication function
  >
  >    Args:
  >        a: first integer
  >        b: second integer
  >
  >    Returns:
  >        The return value. a * b
  >    """
  >    return (a * b)
  >
  >
  >def div(a, b):
  >    """My division function
  >
  >    Args:
  >        a: first integer
  >        b: second integer
  >
  >    Returns:
  >        The return value. a / b
  >    """
  >    return int(a / b)
  >
  >$ ./1-calculation.py
  >10 + 5 = 15
  >10 - 5 = 5
  >10 * 5 = 50
  >10 / 5 = 2
  >$

* ***2-args.py***: Prints the number of and the list of its arguments.
  * The output is:
    * Number of argument(s) followed by **argument** (if number is one) or **arguments** (otherwise), followed by
    * **":"** or **"."** if no arguments were passed) followed by
    * A new line, followed by (if at least one argument),
    * One line per argument:
      * The position of the argument (starting at **:1:**) followed by **":"**, followed by the argument value and a new line
  * Can't be executed when imported.
  * The number of elements of **argv** can be retrieved by using: **len(argv)**.
  *Example:*
    >$ ./2-args.py 
    >0 arguments.
    >$ ./2-args.py Hello
    >1 argument:
    >1: Hello
    $ ./2-args.py Hello Holberton School 98 Battery street
    >6 arguments:
    >1: Hello
    >2: Holberton
    >3: School
    >4: 98
    >5: Battery
    >6: street

* ***3-infinite_add.py***: Prints the result of the addition of all arguments.
  * The output is the result of the addition of all arguments, followed by a new line.
  * Argumets are casted ito integers by **int()**.
  * Can't be executed when imported.
  * Can handle big numbers.
  *Example:*
  >$ ./3-infinite_add.py
  >0
  >$ ./3-infinite_add.py 79 10
  >89
  >./3-infinite_add.py 79 10 -40 -300 89
  >-162
  >$

* ***4-hidden_discovery.py***: Prints all the names defined by the compiled module hidden_4.pyc.
  * Prints one name per line, in alpha order.
  * Prints only names that do *not* start with **__**.
  * Can't be executed when imported.
  *Example:*
  >$ ./4-hidden_discovery.py | sort
  >my_secret_santa
  >print_holberton
  >print_school
  >$

* ***5-variable_load.py***: Imports the variable a from the file variable_load_5.py and prints its value.
  * __*__ or __\_\_import\_\___ not used for importing.
  * This code is not executed when imported.
  *Example:*
  >$ cat variable_load_5.py
  >$ #!/usr/bin/python3
  >$ a = 98
  >$ """Simple variable
  >$ """
  >
  >$ ./5-variable_load.py
  >98
  >$
