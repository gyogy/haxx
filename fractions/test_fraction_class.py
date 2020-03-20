import unittest
from fraction_class import Fraction

class TestFractionClass(unittest.TestCase):

	def test_for_valid_input(self):

		err = None

		try:
			test = Fraction(4, 0)
		except Exception as e:
			err = e

		self.assertIsNotNone(err)

	def test_string_casting(self):

		result = str(Fraction(3, 4))
		expected = '3/4'

		self.assertEqual(result, expected)

	def test_fraction_simplification(self):

		result = Fraction(10, 12).simplify()
		expected = Fraction(5, 6)

		self.assertEqual(result, expected)

	def test_fraction_addition(self):

		fr1 = Fraction(1, 2)
		fr2 = Fraction(2, 3)

		result = fr1 + fr2
		expected = Fraction(7, 6)

		self.assertEqual(result, expected)

	def test_fraction_sorting(self):
		fr1 = Fraction(1, 2) 
		fr2 = Fraction(1, 3) 
		fr3 = Fraction(2, 3)

		fractions = [fr1, fr2, fr3]

		result = sorted(fractions)
		expected = [fr2, fr1, fr3]

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()