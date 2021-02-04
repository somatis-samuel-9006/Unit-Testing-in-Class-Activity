import unittest
import basic_calculator

class TestBasicCalculator(unittest.TestCase):
    def test_addition(self):
        err_string = "Invalid input"
        self.assertEqual(basic_calculator.addition(10,5), 15)
        self.assertEqual(basic_calculator.addition(-5,10), 5)
        self.assertEqual(round(basic_calculator.addition(3.4,2.8), 2), 6.2)
        self.assertEqual(basic_calculator.addition("a","b"),  err_string)
        self.assertEqual(basic_calculator.addition(1, "2"), err_string)
    
    def test_subtraction(self):
        err_string = "Invalid input"
        self.assertEqual(basic_calculator.subtraction(5,15), -10)
        self.assertEqual(basic_calculator.subtraction(10,2), 8)
        self.assertEqual(round(basic_calculator.subtraction(7.8,6), 2), 1.8)
        self.assertEqual(basic_calculator.subtraction(10,10), 0)
        self.assertEqual(basic_calculator.subtraction("a","b"), err_string)

    def test_multiplication(self):
        err_string = "Invalid input"
        self.assertEqual(basic_calculator.multiplication(10,5), 50)
        self.assertEqual(basic_calculator.multiplication(-5,10), -50)
        self.assertEqual(round(basic_calculator.multiplication(3.7,6.3), 2), 23.31)
        self.assertEqual(basic_calculator.multiplication("a","b"), err_string)
        self.assertEqual(basic_calculator.multiplication(1, "2"), err_string)
    
    def test_division(self):
        err_string = "Invalid input"
        self.assertEqual(basic_calculator.division(10,2), 5.0)
        self.assertEqual(basic_calculator.division(-5, 2), -2.5)
        self.assertEqual(round(basic_calculator.division(20,30), 2), 0.67)
        self.assertEqual(round(basic_calculator.division(6.4,3.4), 2), 1.88)
        self.assertEqual(basic_calculator.division(10,0), err_string)
        self.assertEqual(basic_calculator.division("a","b"), err_string)





if __name__ == '__main__':
    unittest.main()