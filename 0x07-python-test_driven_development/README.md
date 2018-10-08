# 0x07. Python - Test-driven Development
---
## Description

During this project I will learn:
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements for Python scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `PEP 8` style (version 1.7.*)
- All files must be executable
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)’`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)’`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)’` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)’`)

## Requirements for Python test cases

- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)’`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)’`)

---
File|Task
---|---
0-add_integer.py, tests/0-add_integer.txt| A function that adds 2 integers
2-matrix_divided.py, tests/2-matrix_divided.txt| A function that divides all elements of a matrix
3-say_my_name.py, tests/3-say_my_name.txt | A function that prints `My name is <first name> <last name>`
4-print_square.py, tests/4-print_square.txt | A function that prints a square with the character `#`
5-text_indentation.py, tests/5-text_indentation.txt | A function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
tests/6-max_integer_test.py | Unittests for the function `def max_integer(list=[]):`

## Author
Essence Boayue