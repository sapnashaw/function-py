#10. What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?\
    
   # The functions map(), reduce(), and filter() in Python are used for processing iterables, but they serve different purposes. Here's a breakdown of their differences:

#1. map()
"""
purpose: Applies a function to each item in an iterable and returns an iterator of the transformed values.
Output: Transformed values (same length as input).
Usage: When you want to modify or transform each item in a sequence.
Example:
"""

numbers = [1, 2, 3]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # Output: [1, 4, 9]
"""
2. filter()
Purpose: Filters items from an iterable based on a function that returns True or False. Only items that return True are included.
Output: A subset of the original iterable (same or fewer elements).
Usage: When you need to filter out elements from a sequence based on a condition.
Example:
"""

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

"""
3. reduce() (from functools module)
Purpose: Reduces an iterable to a single cumulative value by applying a function that takes two arguments. It repeatedly applies the function to the items, accumulating a final result.
Output: A single value.
Usage: When you want to aggregate or combine all elements into a single result (e.g., sum, product, etc.).
Example:
"""
from functools import reduce
numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 10

"""
Key Differences:
map() transforms each item and returns a modified iterable.
filter() selects specific items based on a condition and returns a subset of the original iterable.
reduce() aggregates all items to produce a single result.
Each function serves a unique role in functional programming and helps to write concise, readable code for data transformations and processing.
"""
