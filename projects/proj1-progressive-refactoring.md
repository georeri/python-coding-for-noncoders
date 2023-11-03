# Coding for Noncoders: Project - Progressive Refactoring

## Introduction

In this self-paced lab assignment, you will develop an application in Python that reads data from a CSV file, processes the data, and writes the processed data to either a CSV or JSON file. This assignment is divided into four phases, each building upon the previous one to improve code structure, modularity, and functionality by progressively refactoring procedural code into Object-Oriented code.

Estimated time to complete: 30 minutes or less.

## Prerequisites

- You have completed all 9 introductory [labs](../labs/), or otherwise are familiar with basic Python programming concepts and syntax.
- A computer with Python installed. If you haven't installed Python, please refer to the [official Python downloads](https://www.python.org/downloads/) page and follow the installation instructions for your platform.

## Phase 1: Simple Data Processing

In this phase, you will create a procedural Python script that reads data from a CSV file, performs some simple processing, and writes the processed data to another CSV file.

### Tasks:

1. Create Python file named `data-processor.py`.
2. Create CSV file named `input_data.csv`, and populate it with the contents below.
3. Read data from the input CSV file named `input_data.csv`.
4. Perform a simple processing step, for example, adding a new column that is the sum of the first 2 columns.
5. Write the processed data to an output CSV file named `output_data.csv`.

**Contents of `input_data.csv`:**

```
Col1,Col2,Col3
5,10,15
7,14,21
8,16,24
3,6,9
```

#### Task 1: Read Data from a CSV file

```python
import csv

# Read data from the input CSV file
with open("input_data.csv", "r") as input_file:
    reader = csv.DictReader(input_file)
    data = [row for row in reader]
```

#### Task 2: Simple Data Processing

```python
# Perform simple processing
processed_data = []
for row in data:
    # Example: Add a new column 'Total' by summing the first two columns
    total = int(row["Col1"]) + int(row["Col2"])
    row["Total"] = total
    processed_data.append(row)
```

#### Task 3: Write Processed Data to Another CSV file

```python
# Write the processed data to the output CSV file
with open("output_data.csv", "w") as output_file:
    fieldnames = reader.fieldnames + ["Total"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed_data)
```

## Phase 1 code summary

**Contents of: `data-processor.py`**

```python
import csv

# Read data from the input CSV file
with open("input_data.csv", "r") as input_file:
    reader = csv.DictReader(input_file)
    data = [row for row in reader]

# Perform simple processing
processed_data = []
for row in data:
    # Example: Add a new column 'Total' by summing the first two columns
    total = int(row["Col1"]) + int(row["Col2"])
    row["Total"] = total
    processed_data.append(row)

# Write the processed data to the output CSV file
with open("output_data.csv", "w") as output_file:
    fieldnames = reader.fieldnames + ["Total"]
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed_data)

```

### Code walkthrough

This Python code performs a specific task: it reads data from an input CSV file, processes the data by adding a new "Total" column, and then writes the processed data to an output CSV file. Let's break down the code into logical blocks to explain what each part does:

**1. Importing the necessary module:**

- The code begins by importing the `csv` module, which provides functionality to work with CSV (Comma-Separated Values) files.

**2. Reading data from the input CSV file:**

- It opens the "input_data.csv" file for reading using the `open()` function.
- The `with` statement ensures that the file is properly closed after reading.
- It uses `csv.DictReader` to read the data. This means that each row from the CSV file is treated as a dictionary where column headers are used as keys.
- The data is then stored in the `data` variable as a list of dictionaries, where each dictionary represents a row of data.

**3. Performing simple data processing:**

- It initializes an empty list called `processed_data` to store the processed data.
- It iterates over each row in the `data` list.
- Inside the loop, it calculates a new value for the "Total" column by summing the values of "Col1" and "Col2" from the current row.
- The "Total" value is added to the current row's dictionary.
- The processed row is then appended to the `processed_data` list.

**4. Writing the processed data to the output CSV file:**

- It opens the "output_data.csv" file for writing using the `open()` function.
- Similar to reading, the `with` statement is used to ensure proper file handling.
- It creates a list called `fieldnames` that contains the headers from the input CSV file (retrieved from `reader.fieldnames`) and appends "Total" to it.
- It uses `csv.DictWriter` to write data back to a CSV file, specifying the fieldnames.
- The `writeheader()` method is called to write the header row with column names.
- The `writer.writerows(processed_data)` line writes the processed data to the output CSV file. Each dictionary in `processed_data` is treated as a row, and the keys are matched with the column headers.

## Phase 2: Code Refactoring with Functions

In this phase, you will refactor the code from Phase 1 into discrete, testable functions.

### Tasks:

1. Create a function `read_csv(filename)` that reads data from a CSV file and returns it as a list of lists.
2. Create a function `process_data(data)` that processes the data (e.g., adding total column).
3. Create a function `write_csv(data, fieldnames, filename)` that writes the processed data to a CSV file.
4. Add boilerplate code that tests the functions and protects you from accidentally invoking code

#### Task 1: Create the `read_csv` function

```python
def read_csv(filename):
    with open(filename, "r") as input_file:
        reader = csv.DictReader(input_file)
        return [row for row in reader]
```

#### Task 2: Create the `process_data` function

```python
def process_data(data):
    processed_data = []
    for row in data:
        total = int(row["Col1"]) + int(row["Col2"])
        row["Total"] = total
        processed_data.append(row)
    return processed_data
```

#### Task 3: Create the `write_csv` function

```python
def write_csv(data, fieldnames, filename):
    with open(filename, "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_data)
```

#### Task 4: Execute the functions in boilerplate code

```python
if __name__ == "__main__":
    data = read_csv("input_data.csv")
    processed_data = process_data(data)
    # Read the keys from the first row, these are our column names
    processed_data_fieldnames = processed_data[0].keys()
    write_csv(processed_data, processed_data_fieldnames, "output_data.csv")
```

## Phase 2 code summary

**Contents of: `data-processor.py`**

```python
import csv


def read_csv(filename):
    with open(filename, "r") as input_file:
        reader = csv.DictReader(input_file)
        return [row for row in reader]


def process_data(data):
    processed_data = []
    for row in data:
        total = int(row["Col1"]) + int(row["Col2"])
        row["Total"] = total
        processed_data.append(row)
    return processed_data


def write_csv(data, fieldnames, filename):
    with open(filename, "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_data)


if __name__ == "__main__":
    data = read_csv("input_data.csv")
    processed_data = process_data(data)
    # Read the keys from the first row, these are our column names
    processed_data_fieldnames = processed_data[0].keys()
    write_csv(processed_data, processed_data_fieldnames, "output_data.csv")

```

### Code walkthrough

This Python code is structured into functions and is designed to perform a specific task, which is reading data from an input CSV file, processing the data by adding a new "Total" column, and then writing the processed data to an output CSV file. Let's break down the code into logical blocks to explain what each part does:

**1. Importing the necessary module:**

- The code begins by importing the `csv` module, which provides functionality to work with CSV (Comma-Separated Values) files.

**2. Defining functions:**

- The code defines three functions: `read_csv`, `process_data`, and `write_csv`. Functions are reusable blocks of code that perform specific tasks.

**3. The `read_csv` function:**

- This function takes a `filename` as an argument, representing the name of the input CSV file.
- It opens the specified CSV file for reading using the `open()` function within a `with` statement. The `with` statement ensures that the file is properly closed after reading.
- It uses `csv.DictReader` to read the data. This means that each row from the CSV file is treated as a dictionary where column headers are used as keys.
- The function returns the data as a list of dictionaries, where each dictionary represents a row of data.

**4. The `process_data` function:**

- This function takes `data` as an argument, which is expected to be a list of dictionaries representing CSV data.
- It initializes an empty list called `processed_data` to store the processed data.
- It iterates over each row in the `data` list.
- Inside the loop, it calculates a new value for the "Total" column by summing the values of "Col1" and "Col2" from the current row.
- The "Total" value is added to the current row's dictionary.
- The processed row is then appended to the `processed_data` list.
- The function returns the `processed_data` list.

**5. The `write_csv` function:**

- This function takes three arguments: `data` (the data to be written to the output CSV file), `fieldnames` (the column headers), and `filename` (the name of the output CSV file).
- It opens the specified CSV file for writing using the `open()` function within a `with` statement to ensure proper file handling.
- It creates a `csv.DictWriter` object, specifying the fieldnames to write in the CSV file.
- It writes the header row (column names) to the output file using the `writeheader()` method.
- Finally, it writes the data from the `data` list to the output CSV file using the `writer.writerows()` method.

**6. The `if __name__ == "__main__":` block:**

- This block is used to define the code that should be executed when the script is run.
- It calls the `read_csv` function to read data from the "input_data.csv" file and stores the data in the `data` variable.
- It then calls the `process_data` function to process the data and stores the processed data in the `processed_data` variable.
- It extracts the fieldnames (column names) from the first row of the processed data.
- Finally, it calls the `write_csv` function to write the processed data to the "output_data.csv" file, specifying the processed data, fieldnames, and the output file name.

## Phase 3: Refactor into a Class

In this phase, you will refactor the functions from Phase 2 into a single class that retains the same functionality.

### Tasks:

1. Create a class named `DataProcessor`.
2. Move and refactor the `read_csv`, `process_data`, and `write_csv` functions into this class as methods that use instance variables instead of parameters.
3. Refactor boilerplate code to test the class and its methods

#### Task 1: Create the `DataProcessor` class

```python
class DataProcessor:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.data = []
        self.processed_data = []
        self.processed_data_fieldnames = []
```

#### Task 2a: Move and refactor the `read_csv` function to an instance method

```python
class DataProcessor:
    # Previous contents hidden for brevity

    def read_csv(self):
        with open(self.input_filename, "r") as input_file:
            reader = csv.DictReader(input_file)
            self.data = [row for row in reader]
```

#### Task 2b: Move and refactor the `process_data` function to an instance method

```python
class DataProcessor:
    # Previous contents hidden for brevity

    def process_data(self):
        for row in self.data:
            self.processed_data_fieldnames = row.keys()
            total = int(row["Col1"]) + int(row["Col2"])
            row["Total"] = total
            self.processed_data.append(row)
```

#### Task 2c: Move and refactor the `write_csv` function to an instance method

```python
class DataProcessor:
    # Previous contents hidden for brevity

    def write_csv(self):
        with open(self.output_filename, "w") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=self.processed_data_fieldnames)
            writer.writeheader()
            writer.writerows(self.processed_data)
```

#### Task 3: Refactor boilerplate code to test the class and its methods

```python
if __name__ == "__main__":
    processor = DataProcessor("input_data.csv", "output_data.csv")
    processor.read_csv()
    processor.process_data()
    processor.write_csv()
```

## Phase 3 code summary

**Contents of: `data-processor.py`**

```python
import csv


class DataProcessor:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.data = []
        self.processed_data = []
        self.processed_data_fieldnames = []

    def read_csv(self):
        with open(self.input_filename, "r") as input_file:
            reader = csv.DictReader(input_file)
            self.data = [row for row in reader]

    def process_data(self):
        for row in self.data:
            self.processed_data_fieldnames = row.keys()
            total = int(row["Col1"]) + int(row["Col2"])
            row["Total"] = total
            self.processed_data.append(row)

    def write_csv(self):
        with open(self.output_filename, "w") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=self.processed_data_fieldnames)
            writer.writeheader()
            writer.writerows(self.processed_data)


if __name__ == "__main__":
    processor = DataProcessor("input_data.csv", "output_data.csv")
    processor.read_csv()
    processor.process_data()
    processor.write_csv()

```

### Code walkthrough

This Python code defines a class called `DataProcessor`, which is used to read data from an input CSV file, process the data by adding a new "Total" column, and then write the processed data to an output CSV file. Let's break down the code into logical blocks to explain what each part does:

**1. Importing the necessary module:**

- The code begins by importing the `csv` module, which provides functionality to work with CSV (Comma-Separated Values) files.

**2. Defining the `DataProcessor` class:**

- The `DataProcessor` class is defined, encapsulating the entire process.
- The class has an `__init__` method, which is the constructor. It initializes the class with input and output filenames, empty data and processed_data lists, and an empty processed_data_fieldnames list. This method is automatically called when an object of the class is created.

**3. `read_csv` method:**

- The `read_csv` method is used to read data from the input CSV file.
- It opens the input CSV file (specified in `self.input_filename`) for reading using the `open()` function within a `with` statement to ensure proper file handling.
- It uses `csv.DictReader` to read the data. This means that each row from the CSV file is treated as a dictionary where column headers are used as keys.
- The data is stored in the `self.data` attribute of the class.

**4. `process_data` method:**

- The `process_data` method is used to process the data by adding a new "Total" column to each row.
- It iterates over each row in the `self.data` list.
- It calculates a new value for the "Total" column by summing the values of "Col1" and "Col2" from the current row.
- The "Total" value is added to the current row's dictionary, and the processed row is appended to the `self.processed_data` list.
- It also sets `self.processed_data_fieldnames` to store the column names from the first row of data.

**5. `write_csv` method:**

- The `write_csv` method is used to write the processed data to the output CSV file.
- It opens the output CSV file (specified in `self.output_filename`) for writing using the `open()` function within a `with` statement to ensure proper file handling.
- It creates a `csv.DictWriter` object, specifying the fieldnames to write in the CSV file (retrieved from `self.processed_data_fieldnames`).
- It writes the header row (column names) to the output file using the `writeheader()` method.
- Finally, it writes the data from the `self.processed_data` list to the output CSV file using the `writer.writerows()` method.

**6. The `if __name__ == "__main__":` block:**

- This block is used to define the code that should be executed when the script is run.
- It creates an instance of the `DataProcessor` class, specifying the input and output filenames as arguments.
- It calls the `read_csv` method to read data from the input CSV file and stores the data in the `self.data` attribute.
- It then calls the `process_data` method to process the data, setting `self.processed_data` and `self.processed_data_fieldnames`.
- Finally, it calls the `write_csv` method to write the processed data to the output CSV file.

## Phase 4: CSV to JSON Conversion with Design Patterns

In this final phase, you will extend the DataProcessor class to add the ability to switch between CSV and JSON data formats using the [strategy design pattern](https://refactoring.guru/design-patterns/strategy).

### Tasks:

1. Refactor the `__init__` method of the `DataProcessor` class to require a strategy class as an input parameter. Add type hints
2. Add type hints to the class variables to be clear, explicit, and enable IDEs to interrogate your code better.
3. Refactor the `write_csv` method to `write_data` that writes data using the provided strategy class.
4. Create a `CSVFormat` strategy class that will be responsible for writing data to a CSV file.
5. Create a `JSONFormat` strategy class that will be responsible for writing data to a JSON file.
6. Refactor boilerplate code to test the class and its new methods.

#### Task 1: Refactor the `__init__` method

```python
import csv
import json
from typing import List, Dict


class DataProcessor:
    def __init__(self, input_filename, output_filename, format_strategy):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.data = []
        self.processed_data = []
        self.processed_data_fieldnames = []
        self.format_strategy = format_strategy()
```

#### Task 2: Add type hints to the class variables

```python
import csv
import json
from typing import List, Dict


class DataProcessor:
    input_filename: str
    output_filename: str
    data: List[Dict]
    processed_data: List[Dict]
    processed_data_fieldnames: List[str]

    def __init__(self, input_filename, output_filename, format_strategy):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.data = []
        self.processed_data = []
        self.processed_data_fieldnames = []
        self.format_strategy = format_strategy()
```

#### Task 3: Refactor the `write_csv` method to `write_data`

```python
# Import statements hidden for brevity

class DataProcessor:
    # Previous contents hidden for brevity

    def write_data(self):
        with open(self.output_filename, "w") as output_file:
            self.format_strategy.write(self.processed_data, output_file)
```

#### Task 4: Create a `CSVFormat` strategy class

```python
class CSVFormat:
    def get_fieldnames(self, data):
        fieldnames = []
        for row in data:
            fieldnames = row.keys()
            break
        return fieldnames

    def write(self, data, output_file):
        fieldnames = self.get_fieldnames(data)
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
```

#### Task 5: Create a `JSONFormat` strategy class

```python
class JSONFormat:
    def write(self, data, output_file):
        json.dump(data, output_file, indent=4)
```

#### Task 6: Refactor boilerplate code to test your changes

```python
if __name__ == "__main__":
    input_file = "input_data.csv"

    output_file = "output_data.csv"
    csv_processor = DataProcessor(input_file, output_file, CSVFormat)
    csv_processor.read_csv()
    csv_processor.process_data()
    csv_processor.write_data()

    # Switch to JSON output
    output_file = "output_data.json"
    json_processor = DataProcessor(input_file, output_file, JSONFormat)
    json_processor.read_csv()
    json_processor.process_data()
    json_processor.write_data()
```

## Phase 4 code summary

**Contents of: `data-processor.py`**

```python
import csv
import json
from typing import List, Dict


class DataProcessor:
    input_filename: str
    output_filename: str
    data: List[Dict]
    processed_data: List[Dict]
    processed_data_fieldnames: List[str]

    def __init__(self, input_filename, output_filename, format_strategy):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.data = []
        self.processed_data = []
        self.processed_data_fieldnames = []
        self.format_strategy = format_strategy()

    def read_csv(self):
        with open(self.input_filename, "r") as input_file:
            reader = csv.DictReader(input_file)
            self.data = [row for row in reader]

    def process_data(self):
        processed_data = []
        for row in self.data:
            self.processed_data_fieldnames = row.keys()
            total = int(row["Col1"]) + int(row["Col2"])
            row["Total"] = total
            processed_data.append(row)
        self.processed_data = processed_data

    def write_data(self):
        with open(self.output_filename, "w") as output_file:
            self.format_strategy.write(self.processed_data, output_file)


class CSVFormat:
    def get_fieldnames(self, data):
        fieldnames = []
        for row in data:
            fieldnames = row.keys()
            break
        return fieldnames

    def write(self, data, output_file):
        fieldnames = self.get_fieldnames(data)
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


class JSONFormat:
    def write(self, data, output_file):
        json.dump(data, output_file, indent=4)


if __name__ == "__main__":
    input_file = "input_data.csv"

    output_file = "output_data.csv"
    csv_processor = DataProcessor(input_file, output_file, CSVFormat)
    csv_processor.read_csv()
    csv_processor.process_data()
    csv_processor.write_data()

    # Switch to JSON output
    output_file = "output_data.json"
    json_processor = DataProcessor(input_file, output_file, JSONFormat)
    json_processor.read_csv()
    json_processor.process_data()
    json_processor.write_data()

```

### Code walkthrough

This Python code defines a class called `DataProcessor` that is used to read data from an input CSV file, process the data by adding a new "Total" column, and then write the processed data to an output file. The code also demonstrates switching between different output data formats (CSV and JSON) by using different format strategies. Let's break down the code into logical blocks to explain what each part does:

**1. Importing the necessary modules and defining type hints:**

- The code begins by importing two modules: `csv` for working with CSV files and `json` for working with JSON files.
- It also uses type hints to specify the types of variables and function arguments. For example, `input_filename: str` indicates that `input_filename` is expected to be a string.

**2. Defining the `DataProcessor` class:**

- The `DataProcessor` class is defined to encapsulate the entire process.
- It includes several attributes, such as `input_filename`, `output_filename`, `data`, `processed_data`, `processed_data_fieldnames`, and `format_strategy`. These attributes are used to store various pieces of data throughout the processing.
- The class has an `__init__` method, which is the constructor. It initializes the class with input and output filenames, empty data and processed_data lists, an empty processed_data_fieldnames list, and a format strategy that will be used to write data.
- The `format_strategy` parameter is a class that will be instantiated later to specify the format in which data should be written.

**3. `read_csv` method:**

- The `read_csv` method is used to read data from the input CSV file.
- It opens the input CSV file (specified in `self.input_filename`) for reading using the `open()` function within a `with` statement to ensure proper file handling.
- It uses `csv.DictReader` to read the data. This means that each row from the CSV file is treated as a dictionary where column headers are used as keys.
- The data is stored in the `self.data` attribute of the class.

**4. `process_data` method:**

- The `process_data` method is used to process the data by adding a new "Total" column to each row.
- It initializes an empty list called `processed_data` to store the processed data.
- It iterates over each row in the `self.data` list.
- It calculates a new value for the "Total" column by summing the values of "Col1" and "Col2" from the current row.
- The "Total" value is added to the current row's dictionary, and the processed row is appended to the `self.processed_data` list.
- It also sets `self.processed_data_fieldnames` to store the column names from the first row of data.

**5. `write_data` method:**

- The `write_data` method is used to write the processed data to the output file.
- It opens the output file (specified in `self.output_filename`) for writing using the `open()` function within a `with` statement to ensure proper file handling.
- It calls the `self.format_strategy.write` method to write the processed data to the output file.

**6. Format strategy classes:**

- The code defines two format strategy classes, `CSVFormat` and `JSONFormat`, that are used to specify the format in which data should be written.
- The `CSVFormat` class provides methods to determine fieldnames and write data in CSV format, while the `JSONFormat` class provides a method to write data in JSON format.

**7. The `if __name__ == "__main__":` block:**

- This block is used to define the code that should be executed when the script is run.
- It specifies the input and output file names for both CSV and JSON formats.
- It creates an instance of the `DataProcessor` class for CSV format, reads the CSV data, processes it, and writes it to an output CSV file.
- It then switches to JSON format, creates another instance of the `DataProcessor` class with the same input data, and writes the processed data to an output JSON file.

## Conclusion

Congratulations! You have completed this self-paced lab assignment. This final code demonstrates a class-based approach to reading, processing, and writing data, with the flexibility to switch between different output formats (CSV and JSON) by using different format strategies. The use of classes and format strategies makes the code modular and extensible, allowing for easy adaptation to various data processing and output needs.
