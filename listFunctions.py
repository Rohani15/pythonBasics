luckyNumbers = [4, 8, 15, 16, 23, 42]
friends = ['k', 'ka', 'j', 'o', 't',]

# extend function. append another list onto another list

friends.extend(luckyNumbers) # add 2 lists together

friends.append('vf') # add another item to the end of the list

friends.insert(2, 'gd') # adds in the middle of the list at a index

friends.remove('j') # removed from the list

# friends.clear() # gets rid of every element in the list

friends.pop() # pops the last item off the list

print(friends)

print(friends.index('t') # gives u the index of an element in the array

print(friends.count('t')) # gives count of how many same elements
      
luckyNumbers.sort() # sorts the array
print(luckyNumbers)

luckyNumbers.reverse() # reverses the order of the list

friends2 = friends.copy() # duplicates the list
print(friends2) 



           
