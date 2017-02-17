'''
Created on Feb 16, 2017

@author: walter.policarpio
'''

import unittest
from app.calculator import Calculator
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,3)
        self.assertEqual(4, result)
 
 
if __name__ == '__main__':
    unittest.main()