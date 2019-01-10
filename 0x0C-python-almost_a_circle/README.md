# 0x0C. Python - Almost a Circle
---
## Description

During this project I will learn:
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function



## Requirements for Python scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `PEP 8` style `(version 1.7.*)`
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
models/base.py | A class called `Base` that other classes can inherit from
models/rectangle.py | A class called `Rectangle` that inherits from `Base`
models/square.py | A class called `Square` that inherits from `Rectangle`
models/\_\_init\_\_.py | Blank init file that makes the directory a module
tests/\_\_init\_\_.py | Blank init file that makes the directory a module
tests/test_models/\_\_init\_\_.py | Blank init file that makes the directory a module
tests/test_models/test_base.py | Contains test cases for `base.py`
tests/test_models/test_rectangle.py | Contains test cases for `rectangle.py`
tests/test_models/test_square.py | Contains test cases for `square.py`


## Author
Essence Boayue [Github](https://github.com/eboayue)|[LinkedIn](https://www.linkedin.com/in/essenceboayue/)|[Twitter](https://twitter.com/girlsaregeeks2)
