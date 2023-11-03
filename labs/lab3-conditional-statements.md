# Coding for Noncoders: Conditional Statements

## Introduction

In this beginner-friendly hands-on lab, you will learn about using conditional statements in Python for decision-making in your code. You will explore how to make choices and perform different actions based on specific conditions. This lab provides a structured learning path and detailed explanations for all the code.

Estimated time to complete: 15 minutes or less.

## Prerequisites

- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Lab Instructions

### Step 1: Open a Text Editor or Integrated Development Environment (IDE)

You can use a simple text editor like Notepad (on Windows) or any code editor/IDE of your choice. Recommended code editors for Python include [Visual Studio Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Step 2: Create a New Python File

1. Open your text editor or IDE.
2. Create a new Python file with the extension `.py`. You can name it something like `conditional_statements.py`.

### Step 3: Learn about Conditional Statements

Conditional statements allow your code to make decisions based on certain conditions. There are two main types of conditional statements in Python: `if` and `if-else`. Let's explore both.

1. **Using `if` Statements:**

   - Create a variable `x` and assign an integer value to it.
   - Write an `if` statement to check if `x` is greater than 10.
   - If the condition is met, print "x is greater than 10."

   ```python
   # Using if Statements
   x = 15

   if x > 10:
       print("x is greater than 10")
   ```

2. **Using `if-else` Statements:**

   - Create a variable `y` and assign an integer value to it.
   - Write an `if-else` statement to check if `y` is greater than 10.
   - If the condition is met, print "y is greater than 10." Otherwise, print "y is not greater than 10."

   ```python
   # Using if-else Statements
   y = 5

   if y > 10:
       print("y is greater than 10")
   else:
       print("y is not greater than 10")
   ```

### Step 4: Combining Conditions with `elif`

You can use the `elif` (short for "else if") statement to specify multiple conditions to be checked one by one. Let's see how it works.

- Create a variable `z` and assign an integer value to it.
- Write an `if-elif-else` statement to check the value of `z`.
- If `z` is greater than 10, print "z is greater than 10."
- If `z` is equal to 10, print "z is equal to 10."
- If none of the above conditions are met, print "z is less than 10."

```python
# Combining Conditions with elif
z = 7

if z > 10:
    print("z is greater than 10")
elif z == 10:
    print("z is equal to 10")
else:
    print("z is less than 10")
```

### Step 5: Conclusion

In this hands-on lab, you learned about using conditional statements (`if`, `if-else`, and `elif`) to make decisions in your Python code. These statements allow you to execute different code blocks based on specific conditions, enabling your programs to perform different actions as needed.

To explore more about conditional statements and control flow in Python, you can refer to the [official Python documentation](https://docs.python.org/3/tutorial/controlflow.html). The documentation provides detailed information and examples on using conditional statements and loops.

Happy coding!
