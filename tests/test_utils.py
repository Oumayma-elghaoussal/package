import unittest
from CSTC.utils import greet_user

class TestUtils(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("oumayma"), "Salut, oumayma! Bienvenue dans CSTC.")
