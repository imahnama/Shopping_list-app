class UserDetails(object):
    """ A class that handles user details"""
    userlist =[]

    def __init__(self):
        self.details={}


    def signup(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password


        for user in self.userlist:
            if username == user['username'] or email == user['email']:
                return "username or email exists"
        else:
            self.details ={'username' : self.username, 'email' : self.email , 'password' :  self.password}
            self.userlist.append(self.details)
            return "registered"



    def login(self,username, password):
        for user in self.userlist:
            print(user)
            if username == user['username']:
                print(user)
                if password == user['password']:
                    return True

        else:
            return False
