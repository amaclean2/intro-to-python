users = []

# complete this function so that it returns a dict with the properties
# name, email, and password
def buildUser(name, email, password) :
    # your code here


# complete this function so that it passes the parameteres from here
# to buildUser and appends what buildUser returns to users
def addUser(name, email, password) :
    # your code here


# complete this function so that it prints "User's name: <users name>"
# for each user in users
def printNames() :
    # your code here


# complete this function so that we add a property with the key
# 'createdDate' and the value date provided in the parameters to each
# user in users
def addCreatedDate(date) :
    # your code here


# BONUS: complete this function so that if a user's email is longer than
# 20 characters we print it
def findLongEmails() :
    # your code here


##-----##

addUser("Johnny Mosely", "jmosely@alpenglow.com", "jmosely")
addUser("Adrien Bellinger", "abellinger@alpenglow.com", "abell")
addUser("Jimmy Chin", "jchin@thenorthface.com", "jchin")
addUser("Tommy Caldwell", "tcaldwell@thenorthface.com", "tcald")
addUser("Dan Schulman", "dan@paypal.com", "dscul")

print("\nPrinting Names\n")
printNames()

addCreatedDate("April 15, 2020")

print("\nPrinting Users\n")
for user in users :
    print(user)

print("\nPrinting Long Emails\n")
findLongEmails()