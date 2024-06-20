# test_arithmetic.py
import unittest
from arithmetic import add, subtract

class TestArithmeticFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
