# Write code in each of these functions that fulfill the following requirements.
# 
# createUser should take the five parameters given and add a new dict to the end of the users list
# 
# authUser shoud take userName and check it against the users list. If a userName matches,
# it should check the password against that user and if that matches then it should return the user.
# Otherwise it should give one of two error messages.
#
# If no user was found matching that userName then it should return "no user found"
# If the password for that user doesn't match then it should return "password is incorrect"


users = []

def createUser(fullName, email, userName, password, phoneNumber) :
    # your code here


def authUser(userName, password) :
    # your code here






createUser(
    "Alayna Floyd",
    "alayna@yahoo.com",
    "alaynaRocks",
    "alaynaRocks234",
    "(513) 472-9164"
)

createUser(
    "Lance Hudson",
    "lhudson@gmail.com",
    "lhudson",
    "z48Fq$3qaM51@",
    "(684) 391-1987"
)

createUser(
    "Grayson Dominguez",
    "gdominguez@amazon.com",
    "gdominguez",
    "Passw0rd.",
    "(123) 456-7890"
)

createUser(
    "Vivian Johns",
    "vivian23@apple.com",
    "vjohns",
    "1234567",
    "(111) 111-1111"
)


print(authUser("vjohns", "1234567"))

print(authUser("gdom", "password."))

print(authUser("lhudson", "123"))

print(authUser("alaynaRocks", "alaynaRocks234"))