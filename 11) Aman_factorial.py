  # factorial of number
def factorial(num):
    # for negative
    if num < 0:
        return
    
    # base condition
    elif num == 0 || n == 1:
        return 1
    
    # calculation
    else:  
        fact = 2
        while num > 2:
            fact *= num
            num -= 1
        return fact

number = int(input("Enter the number : "))
print("factorial of the number is :", factorial(number))
