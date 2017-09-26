import unittest
from app.userdetails import UserDetails
class TestUser(unittest.TestCase):

    def setUp(self):
        """create a setup object for testing"""
        self.user = UserDetails()

    def tearDown(self):
        """Destroy the object after every test"""
        del self.user

    def test_create_user(self):
        self.assertIsInstance(self.user, UserDetails)

    def test_signup_that_checks_for_correct_username(self):
        self.user.signup('nama','muannama25@gmail.com','123456')
        username = self.user.username
        self.assertIs(username,'nama')

    def test_signup_that_checks_for_correct_email(self):
        self.user.signup('nama','muannama25@gmail.com','123456')
        email = self.user.email
        self.assertIs(email,'muannama25@gmail.com')

    def test_login_that_checks_for_correct_user_details(self):
        self.user.signup('nama','muannama25@gmail.com','123456')
        res = self.user.login('nama','123456')
        self.assertTrue(res)

    def test_login_that_checks_for_wrong_username(self):
        self.user.signup('nasra','rahmahalane@gmail.com','2345678')
        res = self.user.login('nasra1','2345678')
        self.assertFalse(res)

if __name__ == '__main__':
    """run the tests"""
    unittest.main()
