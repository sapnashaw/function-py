#5. What are iterators in Python and how do they differ from iterables?

"""
Iterable: An object that can be looped over (e.g., lists, tuples, strings). It has an __iter__() method to return an iterator.

Iterator: An object that produces elements one at a time. It has __next__() to get the next item and raises StopIteration when there are no more items.

Difference: Iterables can be converted to iterators using iter(). Iterators are used to fetch elements sequentially with next().
"""



