class UserList :
    users = []

    def addUser(self, user) :
        self.users.append(user)

    def findUser(self, userName) :
        for (i, user) in enumerate(self.users) :
            print(i, user)