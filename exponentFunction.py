# allow us to take a certian number and raise it to a specific power

def raiseToPower(baseNum, powerNum):
    result = 1 # where we store the actual result of the math
    for index in range(powerNum): # wanna loop through the range of numbers power numbers of time
        result = result * baseNum
    return result

print(raiseToPower(3, 3)) 


