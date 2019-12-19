# 0x04-python-more_data_structures

* ***0-square_matrix_simple.py***: Function that computes the square value of all integers of a matrix.

  * Prototype: __def square_matrix_simple(matrix=[]):__
  * __matrix__ is a 2 dimensional array
  * Returns a new matrix:
    * Same size as __matrix__
    * Each value is the square of the value of the input
  * Initial matrix will not be modified
  * No module imported  
  __Example__  

  ```
  :~/0x04$ cat 0-main.py
  #!/usr/bin/python3
  square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

  matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]

  new_matrix = square_matrix_simple(matrix)
  print(new_matrix)
  print(matrix)

  :~/0x04$ ./0-main.py
  [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  :~/0x04$
  ```  

* ***1-search_replace.py***: Function that replaces all occurrences of an element by another in a new list

  * Prototype: __def search_replace(my_list, search, replace):__
  * __my_list__ is the initial list
  * search is the element to replace in the list
  * __replace__ is the new element
  * No module imported  
  __Example__  
  ```
  :~/0x04$ cat 1-main.py
  #!/usr/bin/python3
  search_replace = __import__('1-search_replace').search_replace

  my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
  new_list = search_replace(my_list, 2, 89)

  print(new_list)
  print(my_list)

  :~/0x04$ ./1-main.py
  [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
  [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
  :~/0x04$
  ```  

* ***2-uniq_add.py***: Function that returns a set of common elements in two sets

  * Prototype: def common_elements(set_1, set_2):
  * You are not allowed to import any module
  __Example__  
  ```
  :~/0x04$ cat 3-main.py
  #!/usr/bin/python3
  common_elements = __import__('3-common_elements').common_elements

  set_1 = { "Python", "C", "Javascript" }
  set_2 = { "Bash", "C", "Ruby", "Perl" }
  c_set = common_elements(set_1, set_2)
  print(sorted(list(c_set)))

  :~/0x04$ ./3-main.py
  ['C']
  :~/0x04$ 
  ```  

* ***4-only_diff_elements.py***: Function that returns a set of all elements present in only one set.

  * Prototype: __def only_diff_elements(set_1, set_2):__
  * No module imported  
  __Example__  
  ```
  :~/0x04$ cat 4-main.py
  #!/usr/bin/python3
  only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

  set_1 = { "Python", "C", "Javascript" }
  set_2 = { "Bash", "C", "Ruby", "Perl" }
  od_set = only_diff_elements(set_1, set_2)
  print(sorted(list(od_set)))

  :~/0x04$ ./4-main.py
  ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
  :~/0x04$
  ```  

* ***5-number_keys.py***: function that returns the number of keys in a dictionary

  * Prototype: __def number_keys(a_dictionary):__
  * No module imported  
  __Example__  
  ```
  :~/0x04$ cat 5-main.py
  #!/usr/bin/python3
  number_keys = __import__('5-number_keys').number_keys

  a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
  nb_keys = number_keys(a_dictionary)
  print("Number of keys: {:d}".format(nb_keys))

  :~/0x04$ ./5-main.py
  Number of keys: 3
  :~/0x04$
  ```  

* ***6-print_sorted_dictionary.py***: Function that prints a dictionary by ordered keys.

  * Prototype: __def print_sorted_dictionary(a_dictionary):__
  * all keys must be strings
  * Keys will be sorted by alphabetic order
  * Only keys of the first level will be sorted (won't sort keys of a dictionary inside the main dictionary)
  * Dictionary values can have any type
  * No module imported  
  __Example__  

  ```
  :~/0x04$ cat 6-main.py
  #!/usr/bin/python3
  print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

  a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
  print_sorted_dictionary(a_dictionary)

  :~/0x04$ ./6-main.py
  Number: 89
  ids: [1, 2, 3]
  language: C
  track: Low level
  guillaume@ubuntu:~/0x04$
  ```  

* ***7-update_dictionary.py***: Function that replaces or adds key/value in a dictionary

  * Prototype: def update_dictionary(a_dictionary, key, value):
  * key argument must be always a string
  * value argument can be any type
  * If a key exists in the dictionary, the value will be replaced
  * If a key doesn’t exist in the dictionary, it will be created
  * No module imported  
  __Example__  
  ```
  :~/0x04$ cat 7-main.py
  #!/usr/bin/python3
  update_dictionary = __import__('7-update_dictionary').update_dictionary
  print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

  a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
  new_dict = update_dictionary(a_dictionary, 'language', "Python")
  print_sorted_dictionary(new_dict)
  print("--")
  print_sorted_dictionary(a_dictionary)

  print("--")
  print("--")

  new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
  print_sorted_dictionary(new_dict)
  print("--")
  print_sorted_dictionary(a_dictionary)

  :~/0x04$ ./7-main.py
  language: Python
  number: 89
  track: Low level
  --
  language: Python
  number: 89
  track: Low level
  --
  --
  city: San Francisco
  language: Python
  number: 89
  track: Low level
  --
  city: San Francisco
  language: Python
  number: 89
  track: Low level
  :~/0x04$ 
  ```  

* ***8-simple_delete.py***: Function that deletes a key in a dictionary.

  * Prototype: def simple_delete(a_dictionary, key=""):
  * key argument will be always a string
  * If a key doesn’t exist, the dictionary won’t change
  * You are not allowed to import any module

  __Example__

  ```
  :~/0x04$ cat 8-main.py
  #!/usr/bin/python3
  simple_delete = __import__('8-simple_delete').simple_delete
  print_sorted_dictionary = \
  __import__('6-print_sorted_dictionary').print_sorted_dictionary

  a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
  new_dict = simple_delete(a_dictionary, 'track')
  print_sorted_dictionary(a_dictionary)
  print("--")
  print_sorted_dictionary(new_dict)

  print("--")
  print("--")
  new_dict = simple_delete(a_dictionary, 'c_is_fun')
  print_sorted_dictionary(a_dictionary)
  print("--")
  print_sorted_dictionary(new_dict)

  :~/0x04$ ./8-main.py
  Number: 89
  ids: [1, 2, 3]
  language: C
  --
  Number: 89
  ids: [1, 2, 3]
  language: C
  --
  --
  Number: 89
  ids: [1, 2, 3]
  language: C
  --
  Number: 89
  ids: [1, 2, 3]
  language: C
  :~/0x04$ 
  ```

* ***9-multiply_by_2.py***: function that returns a new dictionary with all values multiplied by 2

  * Prototype: __def multiply_by_2(a_dictionary):__
  * All values must be integers
  * Returns a new dictionary
  * No module imported

  __Example__

  ```
  guillaume@ubuntu:~/0x04$ cat 9-main.py
  #!/usr/bin/python3
  multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
  print_sorted_dictionary = \
  __import__('6-print_sorted_dictionary').print_sorted_dictionary

  a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
  new_dict = multiply_by_2(a_dictionary)
  print_sorted_dictionary(a_dictionary)
  print("--")
  print_sorted_dictionary(new_dict)

  guillaume@ubuntu:~/0x04$ ./9-main.py
  Alex: 8
  Bob: 14
  John: 12
  Mike: 14
  Molly: 16
  --
  Alex: 16
  Bob: 28
  John: 24
  Mike: 28
  Molly: 32
  guillaume@ubuntu:~/0x04$
  ```

* ***10-best_score.py***: Function that returns a key with the biggest integer value.

  * Prototype: __def best_score(a_dictionary):__
  * All values must be integers
  * If no score is found, returns __None__
  * You can assume all students have a different score
  * No modules imported

  __Example__

  ```
  :~/0x04$ cat 10-main.py
  #!/usr/bin/python3
  best_score = __import__('10-best_score').best_score

  a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
  best_key = best_score(a_dictionary)
  print("Best score: {}".format(best_key))

  best_key = best_score(None)
  print("Best score: {}".format(best_key))

  :~/0x04$ ./10-main.py
  Best score: Molly
  Best score: None
  :~/0x04$ 
  ```

* ***11-mutiply_list_map.py***: Function that converts a Roman numeral to an integer.

  * Prototype __def roman_to_int(roman_string): __
  * The number must be between 1 to 3999.
  * __def roman_to_int(roman_string)__ will return an integer
  * If the roman_string is not a string or None, returns 0

  __Example__
  ```
  :~/0x04$ cat 12-main.py
  #!/usr/bin/python3
  """ Roman to Integer test file
  """
  roman_to_int = __import__('12-roman_to_int').roman_to_int

  roman_number = "X"
  print("{} = {}".format(roman_number, roman_to_int(roman_number)))

  roman_number = "VII"
  print("{} = {}".format(roman_number, roman_to_int(roman_number)))

  roman_number = "IX"
  print("{} = {}".format(roman_number, roman_to_int(roman_number)))

  roman_number = "LXXXVII"
  print("{} = {}".format(roman_number, roman_to_int(roman_number)))

  roman_number = "DCCVII"
  print("{} = {}".format(roman_number, roman_to_int(roman_number)))

  :~/0x04$ ./12-main.py
  X = 10
  VII = 7
  IX = 9
  LXXXVII = 87
  DCCVII = 707
  :~/0x04$ 
  ```
