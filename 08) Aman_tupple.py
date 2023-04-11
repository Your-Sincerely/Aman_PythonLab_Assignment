'''Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
'''

# Creating a tuple:
Tuple = ("First index", 1, 2, 3, "AMAN", True, False, "Last index")

# Functions in tuple:
  # length of tuple
print("Length of tuple", len(Tuple)) 
 # Backward indexing getting element
print("Backward indexing : ", Tuple[-1]) 
  # Forward indexing getting element
print("Forward indexing : ", Tuple[0])  
  # slicing in tuple
print("Slicing in tuple using forward indexing", Tuple[0:2])
print("Printing tuple", Tuple)  # printing tuple

New_Tuple = (1, 2, 3, 4)  # New Tuple
List = [New_Tuple, 1, 2, 34]  # Creating a nested tuple in list
print("nested tuple in list:", List)  # printing tuple in list

# converting tuple into list for mutations
List1 = list(New_Tuple)
print("Changing tuple into list", List1)  # converting tuple into list
List1[1] = "AMAN"  # changing value
print("After changing value : ", List1)

# appending in tuple by changing tuple into list:
List1.append("New element")
New_Tuple = tuple(List1)
print("After appending in tuple : ", New_Tuple)
