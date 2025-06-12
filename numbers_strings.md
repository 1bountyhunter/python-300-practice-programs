# Numbers and Strings in Python:

- Numbers are the strongest forte of python, as python has integers, float, complex numbers and the number precision here is quite high.
- Strings acan be concatenated using operator overloading feature of python.
- Python can handle really very large numbers without fail, or error.
- Python has a math library that can be imported to perform maths operation (aka import math).
    1. math.floor(3.8) #gives the lowest value closer to the given number on the number line i.e. 3
    2. math.ceil(3.8) #gives the closest higher value to the given number on the number line i.e. 4
    3. math.floor(-3.8) #gives the lowest value closer to the given number on the number line i.e. -4
    4. math.ceil(-3.8) #gives the closest higher value to the given number on the number line i.e. -3
    5. math.floor(3.8) #gives the lowest value closer to the given number on the number line i.e. 3
    6. math.trunc(3.8) #gives value that'd point towards zero i.e. 3

- Also python allows multiple types of numbers format: binary, decimal, octal, hexa-decimal
- Binary : 0b1000 is 8
- Decimal is the regular numbers format we use
- Octal : 0o20 is 16
- HexaDecimal : 0xff is 255

Similarly we have various modules like random, math, sys for multiple methods to use in programs and device various outputs

# Strings:

- "strip()" is a method used in python to remove extra white-spaces when collecting any input from user. // Generally in strings.
- .replace("arg1", "arg2") is a method used in python to replace values of arg1 in a string with arg2.
- similarly .count("arg") is a method that is used to return the count of "arg" in the given string.
- Sometimes, when we want to use the same string multiple times in the program, we use formatted strings, with the help of place holders as follows:
//
name = "mahak"
age = 22
print(f"my name is {name} and I am {age} years old")
or 
order = "my name is {} and I am {} years old"
print(order.format(name, age))

- To convert list to strings: 
1. Let a list be list_1 = ["milk", "butter", "cheese", "ghee"]
 print("".join(list_1)) // but this gives the output by concatenating the elements of the list altogether which isn't the most feasible result in most of the cases

2. print(", ".join(list_1)) // tells to seperate the list items using ", ".

- Also when we use special chaacters that are generally reserved for internal working of python, we tend to use raw strings so as to indicate to python compilers that we don't intend to use those special characters as special characters
- eg: print(r"Z:\python4meh\Python_basics")
or
- we opt to use the special symbols with a backslash to avoid the compiler from missunderstanding
- eg: print("Z:\\python4meh\\Python_basics")