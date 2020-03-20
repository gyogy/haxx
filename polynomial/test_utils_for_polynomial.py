import unittest
from utils_for_polynomial import operators_extractor, parser

class Test(unittest.TestCase):

	def test_parser(self):
		string = ' 2x^3 - 3x + 1'

		result = parser(string)
		expected = ['2x3','3x','1']

		self.assertEqual(result, expected)

	def test_operators_extractor(self):
		string = ' 2x^3 - 3x + 1'

		result = operators_extractor(string)
		expected = ['-', '+']

		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()