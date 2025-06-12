# the pycache file created when we import modules or functions is to ensure that the program simply-compiles faster than what it would be if it were doing it from scratch.
# .pyc is for compiled python byte code: generally called frozen binaries
# .pyc files are always created only for imported files so as to optimize the program speed ?
# standard python is cpython, though there exist multiple other python sub units built upon various other programming languages. 

# PVM is the python virtual machine used by python to generate machine level codes for any given code

# byte code is not machine code. It's a python specific interpretation.
# 90% cases uses cpython(standard implementation), but also has jython, ironPython, stackless(for concurrency), PyPy(performance oriented) etc. 
from hello_1 import chai

chai("ginger tea")

'''  
Understanding Python's Internal Workings
When working with Python, let's explore how the language executes code by importing a Python file (hello.py) into another file (chai.py) within the same folder.

Compilation and Execution
Initially, we have a single file (hello.py) that is interpreted and converted into byte code. This byte code is then sent to the Python Virtual Machine (PVM), which converts it into machine code for execution.

Key Takeaways
1. Byte Code Generation: The source code needs to be converted into byte code before it's converted into machine code for execution.
2. Byte Code Characteristics: Byte code is NOT machine code, but rather it is a Python-specific interpretation, only meant for Python virtual machines. Byte code is already compiled, thus has already been checked for errors, syntax, indentation, etc., and thus is generally faster when executed. Byte code is low-level code and is platform/system independent, but language-specific (i.e., only meant for the Python interpreter).

*Importing Modules and __pycache__*
When we import hello.py into chai.py, a new folder (__pycache__) is created, containing a binary file (hello.cpython-312.pyc). This folder is important for the Python Virtual Machine (PVM) to keep track of the files being used from one file to another.

*Understanding __pycache__*
- The .pyc extension signifies compiled Python files and is generally hidden, but in the case of imports of files, it's made visible to keep track of changes within the compiled file and the imported files altogether.
- hello.cpython-312.pyc is a compiled Python file specific to the CPython implementation (version 3.12).
- .cpython is the standard implementation of Python that is used, while a lot more exist for specific uses, such as Jython (a Java derivative of Python) or PyPy (for performance orientation), IronPython, or Stackless.

*Purpose of __pycache__*
The __pycache__ folder stores byte code for imported modules, allowing for faster execution by avoiding repeated compilation or interpretation from scratch whenever required. When new functions or classes or objects are imported from one file to another, the Python system creates a __pycache__ file to store the byte code, as it's easier to access the necessary modules easily if we've them compiled into byte code already (time-efficient).

Additional Insight
The PVM is a runtime engine that keeps on interpreting as we keep on adding or deleting stuff from our code simultaneously.
And interpreting doesn't necessarily assure that the byte code once produced would be updated with the new interpreted code.



Layman explaination :
1. Compilation -> Bytecode -> Interpretation: Python code is compiled into bytecode, which is then interpreted by the PVM.
2. PVM executes bytecode: The PVM plays a crucial role in executing the bytecode, making Python code run.

In summary:

- Compilation converts Python code into bytecode.
- Interpretation involves the PVM executing the bytecode.
- The PVM is the runtime environment that makes Python code run.

Think of it like a translator:

- Compilation translates Python code into bytecode (intermediate language).
- The PVM translates bytecode into machine-specific instructions(execution).
'''
