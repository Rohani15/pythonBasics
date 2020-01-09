# functions (def)

def sayhi(): # all the code that comes after this line is inside this funtion until unindented
        print('wassup')
        
sayhi() # calling the function
    

def names(names, age):
    print(' hello ' + names + ' and is ' + str(age))

names("rohani", 23) 


#RETURN STATEMENT IN FUNCTIONS
#return allow python to return info from a function

def cube(num):
    return (num * num * num) # allows to return a function back to whatever is calling the function
print(cube(3))

result = cube(4) 
print(result)

# return keyword breaks out of the function. codr written after wont run

