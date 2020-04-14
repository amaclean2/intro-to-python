myArray = []

# Complete a function that adds elements to the array, 'myArray'
# only if the length of the array is less than 5.
def addToArray(element) :
    # your code here


# Complete a function that removes the last element from the array
# 'myArray', and returns it unless there is one left, then leave it.
def removeFromArray() :
    # your code here


# Complete a function that returns the index of 'element'.
# If the array isn't that long then return -1.
def getIndex(element) :
    # your code here


# Complete a function that calls getElement() and prints the value
# it returns.
def printIndex(element) :
    # your code here


# Complete a function that removes the element 'element' from the
# array and returns it. If the element doesn't exist, then return -1.
def removeElement(element) :
    # your code here


#-----#

addToArray(5)
print("added 5: ", myArray)

addToArray(12)
print("added 12: ", myArray)

removeFromArray()
print("popped: ", myArray)

removeFromArray()
print("popped: ", myArray)

addToArray(12)
print("added 12: ", myArray)

addToArray(13)
print("added 13: ", myArray)

addToArray(6)
print("added 6: ", myArray)

addToArray(2)
print("added 2: ", myArray)

addToArray(7)
print("added 7: ", myArray)

removeFromArray()
print("popped: ", myArray)

removeFromArray()
print("popped: ", myArray)

print("13: ")
printIndex(13)

print("6: ")
printIndex(13)

elem = removeElement(13)
print("removed 13: ", elem)

elem = removeElement(17)
print("removed 17: ", elem)