import unittest
import basecode

class Testbasecase(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(basecode.calc(3,4), 7)

def main():
    unittest.main()

main()
