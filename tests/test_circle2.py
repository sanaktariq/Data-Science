import unittest
import sys 
import os
sys.path.append(os.path.abspath("."))
import figure_generator.circle2 as circle2

class test_circle2(unittest.TestCase):

    def test_fig_gen(self):
        self.assertEqual(circle2.circle(("rectangle"), (2,2), (10), (5)), [[2, 2], [12, 2], [2, 7], [12, 7]])