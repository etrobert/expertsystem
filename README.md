# expertsystem

Project inspired by a 42 subject.

Made in two days to show what I can do in Python.

Expert System is a logical problem solver.\
It takes as its sole argument a file containing a series of logical statements.\
Such as :

A & B => C\
B\
C | B => A

It then processes it and prints for each variable if it is True, False or unknown.

The program creates a tree for each statement.

ex: A & B => C becomes:

          =>
        /    \
       &      C
      / \
     A   B

It will then go over each statement and try to increase its knowledge about any variable.

If it did learn anything after going through all the statements,
   it will go back to the first one and so on.

usage: python3 expertsystem.py input_file\
Your file should have newline separated logical propositions\
Every operand and variable should be separated with a space
