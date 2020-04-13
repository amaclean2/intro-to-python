class User :
    def __init__(self, name, email, username, password, phone) :
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.phone = phone

    def changeName(self, newName) :
        self.name = newName

    def getName(self) :
        return self.name
    
    def changeEmail(self, newEmail) :
        self.email = newEmail

    def getEmail(self) :
        return self.email

    def changeUsername(self, newUsername) :
        self.username = newUsername

    def getUsername(self) :
        return self.username

    def changePassword(self, newPassword) :
        self.password = newPassword

    def getPassword(self) :
        return self.password

    def changePhone(self, newPhone) :
        self.phone = newPhone

    def getPhone(self) :
        return self.phone

    def printUser(self) :
        print("")
        print("Name: %s" % self.name)
        print("Username: %s" % self.username)
        print("Email: %s" % self.email)
        print("Phone number: %s" % self.phone)