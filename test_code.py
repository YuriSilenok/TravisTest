import unittest
import code

class UT_Sum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(5, code.sum(2,3))

if __name__ == '__main__':
    unittest.main()