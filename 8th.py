#8. What is a lambda function in Python and when is it typically used?

# A lambda function in Python is an anonymous, small function defined using the lambda keyword. It can have any number of arguments but only one expression, which is evaluated and returned. Lambda functions are typically used for short, simple operations that are passed as arguments to other functions or when a function is needed temporarily.


#lambda arguments: expression
#Example:

square = lambda x: x**2
print(square(5))  # Output: 25
#Typical Use Cases:
#As arguments to higher-order functions (e.g., functions that take other functions as inputs):


numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # Output: [1, 4, 9, 16, 25]
#In sorting operations where you need to specify a custom sorting key:


items = [(1, 'apple'), (3, 'orange'), (2, 'banana')]
items.sort(key=lambda x: x[0])
print(items)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'orange')]
#For quick, one-time-use functions: Instead of defining a separate function, a lambda can be used for short operations that are only needed once.

"""
Limitations:
Single Expression: Lambda functions can only contain a single expression, making them less suitable for complex logic.
No Statements: They can't have multiple statements or assignments.
In short, lambda functions are concise and useful for short, simple operations where defining a full function would be unnecessary.

"""#