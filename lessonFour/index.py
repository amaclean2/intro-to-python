from User import User
from UserList import UserList

def getNewUser() :
    fullName = input("full name: ")
    email = input("email: ")
    userName = input("user name: ")
    password = input("password: ")
    phoneNumber = input("phone number: ")

    user = User(fullName, email, userName, password, phoneNumber)
    userList = UserList()
    userList.addUser(user)

    userList.findUser(user.getUsername())

getNewUser()