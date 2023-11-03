# Coding for Noncoders: Data Types and Variables

## Introduction

In this beginner-friendly hands-on lab, you will explore the basic data types in Python and learn how to use variables to store and manipulate data. This lab will provide you with a structured learning path and detailed explanations for all the code.

Estimated time to complete: 15 minutes or less.

## Prerequisites

- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Lab Instructions

### Step 1: Open a Text Editor or Integrated Development Environment (IDE)

You can use a simple text editor like Notepad (on Windows) or any code editor/IDE of your choice. Recommended code editors for Python include [Visual Studio Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Step 2: Create a New Python File

1. Open your text editor or IDE.
2. Create a new Python file with the extension `.py`. You can name it something like `data_types_variables.py`.

### Step 3: Explore Basic Data Types

In Python, there are several basic data types. Let's explore a few of them.

1. **Integers (int):**

   - Create a variable called `my_integer` and assign it an integer value.
   - Use the `type()` function to check the data type of `my_integer`.
   - Print the result.

   ```python
   # Integers (int)
   my_integer = 42
   print(type(my_integer))
   ```

2. **Floating-Point Numbers (float):**

   - Create a variable called `my_float` and assign it a floating-point value.
   - Use the `type()` function to check the data type of `my_float`.
   - Print the result.

   ```python
   # Floating-Point Numbers (float)
   my_float = 3.14
   print(type(my_float))
   ```

3. **Strings (str):**

   - Create a variable called `my_string` and assign it a string value.
   - Use the `type()` function to check the data type of `my_string`.
   - Print the result.

   ```python
   # Strings (str)
   my_string = "Hello, World!"
   print(type(my_string))
   ```

4. **Booleans (bool):**

   - Create a variable called `my_boolean` and assign it a boolean value (`True` or `False`).
   - Use the `type()` function to check the data type of `my_boolean`.
   - Print the result.

   ```python
   # Booleans (bool)
   my_boolean = True
   print(type(my_boolean))
   ```

### Step 4: Performing Basic Operations

You can perform basic operations on variables of different data types. Let's explore a few examples.

1. **Arithmetic Operations:**

   - Create two integer variables, `x` and `y`, and perform addition, subtraction, multiplication, and division operations.
   - Print the results.

   ```python
   # Arithmetic Operations
   x = 10
   y = 5

   addition_result = x + y
   subtraction_result = x - y
   multiplication_result = x * y
   division_result = x / y

   print(addition_result)
   print(subtraction_result)
   print(multiplication_result)
   print(division_result)
   ```

2. **String Concatenation:**

   - Create two string variables, `str1` and `str2`, and concatenate them.
   - Print the result.

   ```python
   # String Concatenation
   str1 = "Hello, "
   str2 = "World!"

   concatenated_string = str1 + str2

   print(concatenated_string)
   ```

### Step 5: Variable Reassignment

In Python, you can change the value of a variable after it has been assigned.

- Reassign the variable `my_integer` with a new integer value.
- Print the updated value and data type.

```python
# Variable Reassignment
my_integer = 100
print(my_integer)
print(type(my_integer))
```

### Step 6: Conclusion

In this hands-on lab, you explored basic data types in Python, including integers, floating-point numbers, strings, and booleans. You also learned how to use variables to store and manipulate data. Python provides a wide range of data types and operations, making it a versatile language for various applications.

To dive deeper into Python's data types and operations, you can explore the [official Python documentation](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator). The documentation provides detailed information on Python's capabilities.

Happy coding!
