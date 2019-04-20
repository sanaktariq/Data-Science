import unittest
import sys
import os
sys.path.append(os.path.abspath("."))
import figure_generator.circle as circle
import numpy as np
import matplotlib.pyplot as plt

class test_circle(unittest.TestCase):

    maxDiff = None

    def test_circle(self):
        self.assertEqual(circle.circle(50, res=1).tolist(), [[50.0, 0.0], [50.0, -1.2246467991473532e-14]], msg=None)
        x = str(circle.circle(50, res=15))
        y = """[[ 5.00000000e+01  0.00000000e+00]
 [ 4.56772729e+01  2.03368322e+01]
 [ 3.34565303e+01  3.71572413e+01]
 [ 1.54508497e+01  4.75528258e+01]
 [-5.22642316e+00  4.97260948e+01]
 [-2.50000000e+01  4.33012702e+01]
 [-4.04508497e+01  2.93892626e+01]
 [-4.89073800e+01  1.03955845e+01]
 [-4.89073800e+01 -1.03955845e+01]
 [-4.04508497e+01 -2.93892626e+01]
 [-2.50000000e+01 -4.33012702e+01]
 [-5.22642316e+00 -4.97260948e+01]
 [ 1.54508497e+01 -4.75528258e+01]
 [ 3.34565303e+01 -3.71572413e+01]
 [ 4.56772729e+01 -2.03368322e+01]
 [ 5.00000000e+01 -1.22464680e-14]]"""
        self.assertEqual(str(x), y)
        
        #print(y)

#print(circle.circle(50, res=15).tolist())

if __name__ == '__main__':
    unittest.main()
