    #a list to hold all shopping lists
shoppinglists = []

class Shoppinglist(object):
    """a class to manage a shopping list"""

    def __init__(self ):
        """ initialize a dictionary to hold the details of a particular list"""
        self.listsdict = {}

    def newlist(self, listname, owner):
        id = randint(1, 10000)
        self.listsdict = {'listname' : listname, 'owner' : owner, 'id': id }
        self.shoppinglists.append(dict(self.listsdict))
        print (shoppinglists, "here")
        res = 'success'
        return res

    def view_lists(self, owner):
        #a new list containing names of lists belonging to  a certain user
        user_shoplist = []
        for s_list in self.shoppinglists:
            if s_list['owner']== owner:
                user_shoplist.append(s_list)
                return user_shoplist
