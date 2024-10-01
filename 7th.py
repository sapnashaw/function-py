#7. What are the advantages of using generators over regular functions?


# Generators offer several advantages over regular functions, especially when handling large data or infinite sequences. Here are the key benefits:

"""
1. Memory Efficiency:
    Generators use lazy evaluation, meaning they yield values one at a time, only when requested. This prevents loading the entire dataset into memory at once, which is crucial for handling large or infinite datasets.
2. Improved Performance:
    Since values are generated on demand, generators are often faster than functions that return entire lists, especially when working with large sequences.
3. State Persistence:
   Generators automatically save their state between calls (thanks to yield), allowing for easy implementation of stateful iterators without manually managing state or writing complex classes.
4. Simpler Code:
   enerators can simplify code for iterating over data, reducing the need for complex data structures and logic to store intermediate results.
5. Support for Infinite Sequences:
   Regular functions cannot return infinite sequences as they would eventually run out of memory, but generators can, since they yield values one at a time without ever storing the full sequence in memory.
Example:

"""
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

# Memory efficient, generates values as needed
#In summary, generators are better for working with large datasets, conserving memory, improving performance, and maintaining simpler, more maintainable code.











Ch