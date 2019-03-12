import unittest

from range_iterator import RangeViaIterator

class RangeViaIteratorTest(unittest.TestCase):
    def test_on_normal_working(self):
        generator = range_via_iterator(1, 10, 3)
        self.assertEqual(1, next(generator))
        self.assertEqual(4, next(generator))
        self.assertEqual(7, next(generator))
        self.assertRaises(StopIteration, lambda: next(generator))

if __name__ == '__main__':
    unittest.main()
