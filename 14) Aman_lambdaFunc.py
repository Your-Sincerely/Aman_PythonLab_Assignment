'''A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''

 # giving only single argument
x = lambda a: a + 10 
print("Adding 10 to a : ", x(5))

 # giving two argument a and b
x = lambda a, b: a * b 
print("Multiplying two numbers", x(4, 5)) 

 # function to multiply the number N times
def double(n): 
     # a times n
    return lambda a: a * n 

 # multiplying number 2, a times
 # giving number of times to multiply
func = double(2) 
print(func(4)) 
