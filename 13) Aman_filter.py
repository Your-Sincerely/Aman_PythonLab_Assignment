'''filter(function, sequence)

Parameters:
function: function that tests if each element of a 
sequence true or not.

sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.

Returns:
returns an iterator that is already filtered.
'''

def function(i):
    if i % 2 == 0:
        return i
    else:
        return False


sequence = [1, 2, 3, 4, 5, 6]

  # filters the elements without using loops
a = filter(function, sequence)

for i in a:
    print(i)
