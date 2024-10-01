#6. Explain the concept of generators in Python and how they are defined.

"""
A generator in Python is a special type of function that returns an iterator, which yields values one at a time using the yield keyword instead of return. Generators allow for lazy evaluation, meaning values are produced only when needed, making them memory-efficient and useful for working with large datasets.

"""

#example:

def count_up_to(n):
    for i in range(1, n+1):
        yield i
#you can iterate over the generator using a loop:


for num in count_up_to(3):
    print(num)




#enerators are efficient and ideal for handling large data or streams without loading everything into memory at once.











