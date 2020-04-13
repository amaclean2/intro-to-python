users = []

def createUser(fullName, email, userName, password, phoneNumber) :
    users.append({
        'fullName': fullName,
        'email': email,
        'userName': userName,
        'password': password,
        'phoneNumber': phoneNumber
    })

def authUser(userName, password) :
    foundUser = False
    passCorrect = False

    for user in users :
        if user['userName'] == userName :
            foundUser = True
            if user['password'] == password :
                passCorrect = True
                selectedUser = user

    if foundUser == False :
        return 'user not found'
    elif passCorrect == False :
        return 'password is incorrect'
    else :
        return selectedUser

def getNewUser() :
    fullName = input("full name: ")
    email = input("email: ")
    userName = input("user name: ")
    password = input("password: ")
    phoneNumber = input("phone number: ")

    createUser(fullName, email, userName, password, phoneNumber)
    printUser(users[len(users) - 1])

def printUser(user) :
    print("")
    print("Name: " + user['fullName'])
    print("User name: " + user['userName'])
    print("Email: " + user['email'])
    print("Phone Number: " + user['phoneNumber'])

getNewUser()

class User :
    def __init__(self, )