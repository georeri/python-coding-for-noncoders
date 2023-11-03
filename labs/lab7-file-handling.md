# Coding for Noncoders: Reading and Writing Files

## Introduction

In this beginner-friendly hands-on lab, you will learn how to read data from files and write data to files using Python. This is an essential skill for working with data and configuration files. This lab provides a structured learning path and detailed explanations for all the code.

Estimated time to complete: 15 minutes or less.

## Prerequisites

- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Lab Instructions

### Step 1: Open a Text Editor or Integrated Development Environment (IDE)

You can use a simple text editor like Notepad (on Windows) or any code editor/IDE of your choice. Recommended code editors for Python include [Visual Studio Code](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### Step 2: Create a New Python File

1. Open your text editor or IDE.
2. Create a new Python file with the extension `.py`. You can name it something like `file_handling.py`.

### Step 3: Reading Data from a File

In Python, you can read data from a file using the `open()` function and various file modes. Let's explore how to read data from a file.

1. **Reading Text from a File:**

   - Create a text file named `sample.txt` and add some text to it.
   - Open the file using the `open()` function with the "r" mode (read mode).
   - Read the contents of the file and print them.

   ```python
   # Reading Text from a File
   file_path = "sample.txt"

   with open(file_path, "r") as file:
       file_contents = file.read()
       print(file_contents)
   ```

2. **Reading Line by Line:**

   - Create a text file with multiple lines of text.
   - Open the file in read mode and read the file line by line.
   - Print each line.

   ```python
   # Reading Line by Line
   file_path = "sample_lines.txt"

   with open(file_path, "r") as file:
       for line in file:
           print(line, end="")
   ```

### Step 4: Writing Data to a File

In Python, you can write data to a file using the `open()` function with different file modes. Let's explore how to write data to a file.

1. **Writing Text to a File:**

   - Open a file named `output.txt` in write mode.
   - Write a string to the file using the `write()` method.

   ```python
   # Writing Text to a File
   output_path = "output.txt"

   with open(output_path, "w") as file:
       file.write("Hello, World!\n")
       file.write("This is a new line.")
   ```

2. **Appending Text to a File:**

   - Open the same `output.txt` file in append mode.
   - Append another string to the file using the `write()` method.

   ```python
   # Appending Text to a File
   with open(output_path, "a") as file:
       file.write("\nAppending more text.")
   ```

### Step 5: Conclusion

In this hands-on lab, you learned how to read and write data to files in Python. This is a fundamental skill for working with external data, configuration files, and more. Understanding file handling is essential for various programming tasks.

To explore more about file handling in Python, you can refer to the [official Python documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files). The documentation provides detailed information and examples on working with files.

Happy coding!
