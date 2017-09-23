import unittest
from app.userdetails import UserDetails
class TestUser(unittest.TestCase):

    def setUp(self):
        """create a setup object for testing"""
        self.user = UserDetails()

    def tearDown(self):
        """Destroy the object after every test"""
        del self.user

    def test_user_created(self):
        self.assertIsInstance(self.user, UserDetails)

    def test_signup(self):
        self.user.signup('nama','muannama25@gmail.com','1234')
        username = self.user.usernameself.assertIs(username,'nama')

if __name__ == '__main__':
    """run the tests"""
    unittest.main()
