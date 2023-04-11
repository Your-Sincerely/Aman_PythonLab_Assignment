 # checking palindrome
def palindrome(string): 
    
      # if string equals reverse string
    if string == string[::-1]:
        print("The given string is palindrome")
    else:
        print("The given string is not palindrome")


# main program
input_string = input("Enter the String : ")  # taking input
palindrome(input_string)
