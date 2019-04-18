import unittest
import os
import sys
sys.path.append(os.path.abspath("."))

class TestFields(unittest.TestCase):

    def test_name_with_space(self):
        self.assertTrue("Sana T", "VALID")
        
    def test_name(self):
        self.assertTrue("Sana", "VALID")
        
    def test_name_integer(self):
        self.assertTrue("sana1", "INVALID")

if __name__ == '__main__':
    unittest.main()

