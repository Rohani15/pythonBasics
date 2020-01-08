import this # zen of python

print("hello world") # how to comment in python



# drawing a shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")



#Variables and data types----------------------------------------------------
characterName = "john" # String Variable
characterAge = "23" # int Variable
print("The character name is " + characterName + " and age is " + characterAge)



# can update the varbales--------------------------------------------------
characterName = "Rohani" # String Variable
print("The character name is " + characterName + " and age is " + characterAge)



#Boolean Values-------------------------------------------------------------
isFemale = True
isMale = False


#Changing Case in a String With Methods----------------------------------
name = "rohani sharma"
print(name.title()) # ==> Rohani Sharma

# A method is an action that python can preform on a piece of data.
# The . after name in name.title() tells python to make the title() method act on the variable name
# title() displays each word in titlecase, where each word begins with a capital letter

name = "Rohani Sharma"
print(name.upper()) #ROHANI SHARMA
print(name.lower()) #rohani sharma



# Adding White Spaces to Strings with Tabs/newlines---------------------------
print("python") #python
print("\tpython") # python
print("python\njava\nC++") #adds a new line in the string (\n)
# (\n\t) tells python to move to another line and start the next line with a tab



# WhiteSpace------------------------------------------------------------------
favoriteLanguage = 'python  '
favoriteLanguage = favoriteLanguage.rstrip()
# (rstrip()) method removes the extra white space



#NUMBERS-----------------------------------------------------------------------
# CAN (+, -, *, /) INTEGERS IN PYTHON

print(3 ** 3) # python uses 2 multiplication symbols to represent exponents
print(3 ** 2) # 9
print(10 ** 6) # 1000000



#Floats----------------------------------------------------------------------
# Python calls any number with a decimal point a float.

print(0.1 + 0.1) # ==> 0.2
print(2 * 0.2) # ==> 0.4



# Avoiding Type Errors with the str() Function-------------------------------
# str() function, which tells Python to represent non-string values as strings:

age = 23 
message = "happy" + str(age) + "bday"

# message = "Happy " + age + "rd Birthday!" will give an error
# When you use integers within strings like this, you need to specify -
# explicitly that you want Python to use the inte- ger as a string of characters.




# Integers in Python 2--------------------------------------------------------
# so in python 2, when u divide 2 ints it returns no remainders so do this
print(3.0 / 2) # do this
print(3 / 2) # dont do this












