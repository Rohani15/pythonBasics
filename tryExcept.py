# try except

try:
    answer = 10/0
    number = int(input("enter a number: ")) # covnerting the string number to an int
    print(number)
except ZeroDivisionError as err: # storing this error as a variable
    print("division by 0") # if the user enters something wrong it catches it and prints invalid on the screen
    print(err) 
except ValueError:
    print("invalid input")
    
#try except block allows the program to try out a piece of code.


# best use is to accept specific errors to make it less broad 
