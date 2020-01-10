# 2d lists and nested 

numberGrid = [   # a 2 dimesnionsal array
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(numberGrid[0][0]) # get 1

for row in numberGrid:
    print(row) # will print out all the rows in the list
    for col in row:
        print(col) # print out every value in this 2d array
        
