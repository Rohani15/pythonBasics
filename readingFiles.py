
employeeFile = open("employees.txt", "r" )

print(employeeFile.readable()) # readable() function shoes is file is readable because file set in read mode
print(employeeFile.readline()) # readline function reads the first line in the file
print(employeeFile.readlines()) # readlines puts all the lines into an array

employeeFile.close() # closes the file. important to do this as some point

# r ==> means only want to read whats in the file
# w ==> means can change the file
# a ==> means append info onto the end of the file
# r+ ==> means read and write 

