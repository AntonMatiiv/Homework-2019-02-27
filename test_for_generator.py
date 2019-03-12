import unittest

from range_generator import range_via_generator

class range_via_generator_test(unittest.TestCase):
    def test_on_normal_working(self):
        generator = range_via_generator(1, 10, 3)
        self.assertEqual(1, next(generator))
        self.assertEqual(4, next(generator))
        self.assertEqual(7, next(generator))
        self.assertRaises(StopIteration, lambda: next(generator))

if __name__ == '__main__':
    unittest.main()
