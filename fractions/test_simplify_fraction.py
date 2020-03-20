import unittest
from simplify_fraction import simplify_fraction

class TestSimplifyFraction(unittest.TestCase):

	def test_3_9ths(self):

		fraction = (3, 9)
		result = simplify_fraction(fraction)
		expected = (1, 3)

		self.assertEqual(result, expected)

	def test_22_3rds(self):

		fraction = (462,63)
		result = simplify_fraction(fraction)
		expected = (22,3)

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()