import unittest
from app.userdetails import UserDetails
class TestUser(unittest.TestCase):

    def setUp(self):
        """create a setup object for testing"""
        self.user = UserDetails()

    def tearDown(self):
        """Destroy the object after every test"""
        del self.user

if __name__ == '__main__':
    """run the tests"""
    unittest.main()
