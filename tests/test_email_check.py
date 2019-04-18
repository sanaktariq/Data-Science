import unittest
import os
import sys
sys.path.append(os.path.abspath("."))

class TestEmail(unittest.TestCase):

    def test_email_with_space(self):
        self.assertTrue("sana tariq@gmail.com", "INVALID")
        
    def test_email(self):
        self.assertTrue("sanatariq@gmail.com", "VALID")
        
    def test_email_missingat(self):
        self.assertTrue("sanatariqgmail.com", "INVALID")

if __name__ == '__main__':
    unittest.main()


