# to run code in terminal write: python -u .\filename.py
print("Hello World!!")


# this is an additional step to understand the imprtance of importing modules and bytecode formation.
def chai(n):
    print(n)

chai("lemon tea")

#variables are also called attributes in python.
# when changes are made in the code after converting it to frozen binaries, we opt to include the changes using the following commands :
# from importlib import reload (IMPORTANT)
# reload(module_name), and now we can use the methods in the designated modules.
chai_one = "lemon tea"
chai_two = "green tea"
chai_three = "ginger tea"
chai_four = "masala chai"