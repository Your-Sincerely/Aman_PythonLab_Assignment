'''map() function: returns a map object(which is an iterator) of the results after
   applying the given function to each item of a given iterable (list, tuple etc.) 
'''

def double(n):
    return n + n


numbers = [1, 2, 3, 4]

  # transforms all the items in list without another iteration
result = map(double, numbers)

print(list(result))
