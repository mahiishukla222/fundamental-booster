# Interactive Personal Data Collector

This Python program collects personal information from the user and displays the collected data along with its **data type** and **memory ID**.
## watch video here :
https://drive.google.com/file/d/1TFaqLkGLQSs09QKcrp2QD4yTbDdzHocw/view?usp=sharing
## Python Code

```python
import datetime

print("Welcome to the interactive personal data collector!")

name = input("enter your name:")
age = int(input("enter your age:"))
height = float(input("enter your height in meters:"))
number = int(input("enter your favorite number:"))

print("Thank you ! Here is the information collected from you:")

print("name: ", name, "(type:", type(name), ", id: ", id(name))
print("age: ", age, "(type:", type(age), ", id: ", id(age))
print("height: ", height, "(type:", type(height), ", id: ", id(height))
print("favorite number: ", number, "(type:", type(number), ", id: ", id(number))

year = datetime.datetime.now().year
birth_year = year - age

print("you were born in the year: ", birth_year,
      "(type:", type(birth_year), ", id: ", id(birth_year))

print("Thank you for using the interactive personal data collector. have a nice day!")
```

## Concepts Used

### 1. `input()`

Used to take information from the user.

```python
name = input("enter your name:")
```

### 2. `int()`

Converts the input into an integer.

```python
age = int(input("enter your age:"))
```

### 3. `float()`

Converts the input into a floating-point number.

```python
height = float(input("enter your height in meters:"))
```

### 4. `type()`

Shows the data type of a variable.

```python
type(age)
```

Example:

```text
<class 'int'>
```

### 5. `id()`

Returns the unique identity/memory identifier of an object during the program's execution.

```python
id(age)
```

### 6. `datetime`

The `datetime` module is used to get the current year.

```python
import datetime

year = datetime.datetime.now().year
```

### 7. Birth Year Calculation

The program calculates the approximate birth year using:

```python
birth_year = year - age
```

For example:

```text
Current Year = 2026
Age = 18

Birth Year = 2026 - 18
           = 2008
```

## Sample Output

```text
Welcome to the interactive personal data collector!
enter your name: Mahi
enter your age: 18
enter your height in meters: 1.65
enter your favorite number: 7

Thank you ! Here is the information collected from you:

name:  Mahi (type: <class 'str'>, id: 123456)
age:  18 (type: <class 'int'>, id: 123457)
height:  1.65 (type: <class 'float'>, id: 123458)
favorite number:  7 (type: <class 'int'>, id: 123459)

you were born in the year:  2008
(type: <class 'int'>, id: 123460)

Thank you for using the interactive personal data collector. have a nice day!
```

> **Note:** The actual `id()` values will be different each time the program runs.

## Requirements

* Python 3.x
* No external packages are required.

## How to Run

1. Install Python 3.
2. Save the program as:

```text
personal_data_collector.py
```

3. Open the terminal in the same folder.
4. Run:

```bash
python personal_data_collector.py
```

## Learning Objectives

This program helps practice:

* Variables
* User input
* Type conversion
* `int`
* `float`
* `str`
* `type()`
* `id()`
* Importing modules
* `datetime`
* Basic calculations
* Printing formatted information

* watch video here :
