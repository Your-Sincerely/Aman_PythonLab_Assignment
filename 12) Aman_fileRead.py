# The open() function returns a file object, which has a read() method for reading the content of the file:

# Open and writing a new file in python:
file = open("NewFile.txt", 'w')

# this line will be written in the new file.
writing_file = "This is the content which is written on the file" \
               "\nHello Bootstrap"

  # to write in the file
writeFile = file.write(writing_file)

 # closing file
file.close() 

# opening file and reading file in python:
file = open("NewFile.txt", "r")

 # reading all the lines of the file
print(file.read()) 

  # printing lines as list
  # printing only first line - ending the pointer at the end of the 1st line after reading
print(file.readlines())
 
  # giving the index to print the line
print(file.readline(5))  

# finding the length of the text file (total characters)
print(len(file.read())) 

# finding the length of the text file (total lines in the file)
print(len(file.readlines()))  
file.close()  
