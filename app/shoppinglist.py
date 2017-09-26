class Shoppinglist(object):
    """a class to manage a shopping list"""

    #a list to hold all shopping lists
    shoppinglists = []

    def __init__(self ):
        """ initialize a dictionary to hold the details of a particular list"""
        self.listsdict = {}

    def newlist(self, listname, owner, listid):
        """ A method to create a new list"""
        for shoplist in self.shoppinglists:
            if shoplist['listname'] == listname and shoplist['owner'] == owner:
                return 'list exists'
        # create the list if there is no list with the provided details
        else:
            self.listsdict = {'listname' : listname, 'owner' : owner, 'listid' : listid}
            self.shoppinglists.append(self.listsdict)
            res = 'success'
            return res

    def view_lists(self, owner):
        """ a method to show lists beonging to a particular user"""
        #a new list containing names of lists belonging to  a certain user
        user_shoplist = []
        for s_list in self.shoppinglists:
            if s_list['owner']== owner:
                user_shoplist.append(s_list)
        return user_shoplist
