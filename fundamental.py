
import datetime
print("Welcome to the interactive personal data collector!")
name = input("enter your name:")
age = int(input("enter your age:"))
height =float(input("enter your height in meters:"))
number = int(input("enter your favorite number:"))

print("Thank you ! Here is the information collected from you:")

print("name: ", name, "(type:", type(name), ", id: ", id(name))
print("age: ", age, "(type:", type(age), ", id: ", id(age))
print("height: ", height, "(type:", type(height), ", id: ", id(height))
print("favorite number: ", number, "(type:", type(number), ", id: ", id(number))

year = datetime.datetime.now().year
birth_year = year - age

print("you were born in the year: ", birth_year, "(type:", type(birth_year), ", id: ", id(birth_year))

print("Thank you for using the interactive personal data collector. have a nice day!")
