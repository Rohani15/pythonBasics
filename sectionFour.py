# program control flow--------------------------------------------------------

_author_ = 'dev'
for i in range(1, 12):
    print("no {} squared is {} and cubed is {:4}".format(i, i**2, i**4))
    print('calculation complete')
    print('try again')
    
    
# rest consitions with if, elif, and else------------------------------------

_author_ = 'dev'
name = input('please enter your name: ')
age = int(input('how old are you, {0}?'.format(name)))
# int() converts string # to an int
print(age)

if age >= 18:
    print('you can vote')
else:
    print('come back in {0}'.format(18-age))


print('guess a # between 1 and 10')
guess=int(input())

if guess < 5:
    print('guess lower')
    guess = int(input())
    if guess == 5:
        print('correct')
    else:
        print('incorrect')
elif guess > 5:
    print('guess higher')
    guess = int(input())
    if guess == 5:
        print('correct')
    else:
        print('incorrect')
else:
    print('you got it correct the first time') 

# a simpler version of writing this code ^^^

if guess != 5:
    if guess < 5:
        print('guess higher')
    else:
        print('go lower')
    guess = int(input())
    if guess == 5:
        print('correct')
    else:
        print('incorrect')
else:
    ('correct on first try') 


# more advanced if, elif, and processing--------------------------------------
x = 'false'
if x:
    print('x is true')
# in python, True is 1 and False is 2
# but in an condition, any non-0 or non-empty values will evaluate to true.

##False: False
##None: False
##0: False
##0.0: False
##empty lists []: False
##empty tuple (): False
##empty string ''/"": False
##empty mapping {}: False

x = input('enter some text')
if x:
    print('you entered {} '.format(x))
else:
    print('you did not enter anything') 


print(not False) # outputs True
print(not True) # outputs False

age = int(input('how old are you'))
if not(age <18):
    print('cant vote')
else:
    print('come back in {0} years'.format(18 - age)) 
    

parrot = 'norwegian blue'
letter = input('enter a chat')

if letter not in parrot:
    print('dont need that letter')
else:
    print('give me an {} '.format(letter))


# if then else challenge question---------------------------------------------
name = input('whats ur name?')
age = int(input('whats ur age {0}?'.format(name)))

if 18 <= age < 31: 
    print('welcome')
else:
    print('sorry') 


# for loops-------------------------------------------------------------------

for i in range(1,20): # last valued specified in a range is not included
    print("i is now {}".format(i))

number = '9,223,372,036,854,775,807'
for i in range(0, len(number)): # len() return the length of a string
    print(number[i]) # print the the character position at i



number = "9,223,372,036,854,775,807"
cleanedNumber = ''
# So, we have to initialize a string variable to hold the digits first or
# python will give an error 
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print("The number is {} ".format(newNumber))


# extending for loops--------------------------------------------------------

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number: # will extract a character that each position in that # string
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
#--------------------------------------------
        
newNumber = int(cleanedNumber)
print(' the # is {}'.format(number)) 
    
for state in ['not pinin', 'no more', 'a stiff', 'bereft of life']:
    print('the parrot is ' + state)
    # print('this parrot is {}'.format(state))

for i in range(0, 100, 5): # the five will skip 5 numbers in the output
    print('i is {}'.format(i))

#nest for loops
for i in range(1,13):
    for j in range(1,13):
        print('{} times {} is {}'.format(i, j, i*j))
    print('===============================') 
    
# the {1} It's a placeholder which will be replaced with the first argument
# to format in the result. {1} would be the second argument and so on.  

# understanding, continue, break and else--------------------------------------
shopping_list = ['milk','pasta','eggs','spam','bread','rice']

#continue stops provessing any line in the block & forces to continue
for item in shopping_list:
    if item == 'spam':
        continue 
    print('buy ' + item)

# break command terminated when it gets to that element
for item in shopping_list:
    if item == 'spam':
        break  
    print('buy ' + item)


meal = ["egg", "bacon", "beans", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item == 'spam':
    print("Can't I have anything without spam in it")


#-------
# Modify the code inside this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break





# argumented Assignment------------------------------------------------------------
number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))



# argumented Assignment in a loop------------------------------------------------------------


# while loops---------------------------------------------------------------




























