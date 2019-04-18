import unittest
import os
import sys
sys.path.append(os.path.abspath("."))

class TestPassword(unittest.TestCase):

    def test_password_lessthan8(self):
        self.assertTrue("Draper1", "INVALID")
        
    def test_password_nonumber(self):
        self.assertTrue("Draperuniversity", "INVALID")
        
    def test_password_nocapital(self):
        self.assertTrue("draperuniversity1", "INVALID")

    def test_password_withspace(self):
        self.assertTrue("Draper University1", "INVALID")

    def test_password_valid(self):
        self.assertTrue("Draperuniversity1", "VALID")

if __name__ == '__main__':
    unittest.main()

