""" A class that handles user details"""
class UserDetails(object):


    """a list that holds all users"""
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
            print(self.userlist)
            return "registered"


    def login(self,username, password):
        for user in self.userlist:
            if user['username'] == username:
                print(user)
                if user['password'] == password:
                    return True
        else:
            return False
