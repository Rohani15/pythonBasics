# notes-----------------------------------------------------------------------------
# to access more than 2 values in a list ==> print(cars[0: 2])





# looping through an entire list-----------------------------------------------------
magicians = ['alice', 'davis', 'carolina']

for magician in magicians: # for loop. this line says, pull a name from the list magicians, and store it in the varibale magician
    print(magicians) # told python to print the name that was just stored in magician


magicians = ['alice', 'davis', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick")
    print('keep trying' " + .\n")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# YT ex
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("correct")
        continue # where as break stops the loop
    print(num)


nums = ['1', '2', '3', '4', '5']
for num in nums:
    print(num.title() + 'nice')


# Loop within a Loop-------------------------------------------------------------------
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter) 
