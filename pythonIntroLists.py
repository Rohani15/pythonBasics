# Lists-----------------------------------------------------------------------
# A list is a collection of items in a particular order. (arrays)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)



# Accessing Elements in a List-----------------------------------------------
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # write list name and index to access an element in the array
# ==> treck
print(bicycles[0].title()) # ==> Trek



# Using Individual Values from a List-----------------------------------------
message = 'my first bike was a ' + bicycles[0].title() + '.'
print(message) # my first bike was a Trek.
#this is an ex of adding values from a list like done with other variables



# Changing, adding, and removing elements-----------------------------------

# Modifying Elements in a List
cars = ['a', 'b', 'c']
print(cars)

cars[0] = 'd'
print(cars) 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)



# Adding Elements to a List----------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('bbbb') # to add a new elemtny use append() method
print(motorcycles) 




# Inserting Elements into a List-----------------------------------------------
# You can add a new element at any position in your list by using the insert() method.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'cccc')
print(motorcycles) 




# Removing Elements from a List-----------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1] # using (del)
print(motorcycles) # ==> ['honda', 'suzuki']




# removing an Item Using the pop() Method--------------------------------------------
# using pop() method removes the last item in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

poppedMotorcycle = motorcycles.pop()
print(motorcycles)
print(poppedMotorcycle)
# ==> suzuki: was removed from the end of the list and now sotred in the variable poppedMotorcycle
lastOwned = motorcycles.pop()
print('the last motorcycle i owned was a ' + lastOwned.title() + '.') 
# ==> the last motorcycle i owned was a Yamaha.




# Popping Items from any Position in a List------------------------------------------
# using pop() to remove an item in a list in any position using index.
motorcycles = ['honda', 'yamaha', 'suzuki']
firstOwned = motorcycles.pop(0)
print('the last motorcycle i owned was a ' + firstOwned.title() + '.')




# removing an Item by Value----------------------------------------------------------
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati') # remove() method
print(motorcycles)
# this method only remobes the first occurance and will need a loop to remove if there is more than one




# organizing a list-------------------------------------------------------------------
# using the sort() method to sort a list
cars = ['d', 'c', 'a', 'b']
cars.sort()
print(cars) # ==> a, b, c, d

#sorting this in reverse:
cars.sort(reverse = True)
print(cars)




# Sorting a List Temporarily with the sorted() Function-----------------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.




# Printing a List in Reverse Order---------------------------------------------------
# us the reverse() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)




# Finding the Length of a List-------------------------------------------------------
# use the len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars) # ==> 4





# Keep in mind that whenever you want to access the last item in a list you use the index -1
# print(cars[-1])
# The only time this approach will cause an error is when you request the last item from an empty list:































