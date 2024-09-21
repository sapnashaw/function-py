#1. What is the difference between a function and a method in Python?

"""
In Python, the difference between a function and a method primarily relates to their context and how they are used:

Function
Definition: A function is a standalone block of reusable code that performs a specific task. It is defined using the def keyword.
Scope: Functions can be defined at any level in a program, including globally.
Usage: Functions are called by their name and can take parameters.

"""
#Example:
def add(a, b):
    return a + b

result = add(2, 3)  # Calls the function

"""Method
Definition: A method is similar to a function, but it is associated with an object (instance of a class) or class itself. It is defined within a class.
Scope: Methods are always tied to the class and can access the instance (self) or class (cls) they belong to.
Usage: Methods are called on objects or classes. They can operate on data contained in the object.
"""
#Example.

class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(2, 3)  # Calls the method on the object

"""
Summary
Function: Independent, defined outside of classes.
Method: Dependent on classes or instances, defined within classes.
Both serve to encapsulate behavior, but their context and usage differ significantly.

"""




