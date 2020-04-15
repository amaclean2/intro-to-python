myList = []

# Complete a function that adds elements to the list, 'myList'
# only if the length of the list is less than 5.
def addToList(element) :
    # your code here


# Complete a function that removes the last element from the list
# 'myList', and returns it unless there is one left, then leave it.
def removeFromList() :
    # your code here



# Complete a function that returns the index of 'element'.
# If the list doesn't contain the element then return -1.
def getIndex(element) :
    # your code here



# Complete a function that calls getElement() and prints the value
# it returns.
def printIndex(element) :
    # your code here


# Complete a function that removes the element 'element' from the
# list and returns it. If the element doesn't exist, then return -1.
def removeElement(element) :
    # your code here


#-----#

addToList(5)
print("added 5: ", myArray)

addToList(12)
print("added 12: ", myArray)

removeFromList()
print("popped: ", myArray)

removeFromList()
print("popped: ", myArray)

addToList(12)
print("added 12: ", myArray)

addToList(13)
print("added 13: ", myArray)

addToList(6)
print("added 6: ", myArray)

addToList(2)
print("added 2: ", myArray)

addToList(7)
print("added 7: ", myArray)

removeFromList()
print("popped: ", myArray)

removeFromList()
print("popped: ", myArray)

print("13: ")
printIndex(13)

print("6: ")
printIndex(13)

elem = removeElement(13)
print("removed 13: ", elem)

elem = removeElement(17)
print("removed 17: ", elem)