# if statements

isMale = True
isTall = True

if isMale or isTall:
    print('you are a male or tall or both')
elif isMale and not(isTall):
    print('not a male or tall')
elif not(isMale) and isTall:
    print('ifk')
else:
    print('kdi')


# If statements and comparisons
# instead of boolean values, u can compare values

def maxNum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(maxNum(3,4,5))



# python automatically converts to a string so to print number use
num1 = float(input('enter a num'))
op = input('enter a operator. (+,-,/)')
num2 = float(input('enter a second num'))

#if statement to figure out what operator user picks
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
else:
    print('invalid operator') 


#---------------------------------------
# month conversions

monthConversion = # {} when creating a dictionary
{
    'jan': 'january',
    'feb': 'february', # all theys keys have to be unique 
    'mar': 'march',
    'apr': 'april',
    'mar': 'march',
    'may': 'may',
    'jun': 'june',
    'jul': 'july',
    'aug': 'august',
    'sep': 'september',
    'oct': 'oactober',
    'nov': 'november',
    'dec': 'december',
}
print(monthConversions['nov']) # gives back the full name for november
print(monthConversions.get('dec', 'not a valid key')) # get function same 
# the second value in the .get function is s default value





























    
