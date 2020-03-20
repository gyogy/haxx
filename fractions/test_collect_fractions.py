import unittest
from collect_fractions import (
	collect_fractions,
	normalize_fractions,
	sum_normalized_fractions
	)

class TestNormalizeFractions(unittest.TestCase):

	def test_quarters_and_halfs(self):

		fractions = [(1, 4), (1, 4)]
		result = normalize_fractions(fractions)
		expected = [(4, 16), (4, 16)]
		
		self.assertEqual(result, expected)

class TestSumNormalizedFractions(unittest.TestCase):

	def test_summing_fractions(self):

		frac1 = (7, 16) 
		frac2 = (4, 16)
		result = sum_normalized_fractions(frac1, frac2)
		expected = (11, 16)

		self.assertEqual(result, expected)

	def test_all(self):
		fractions = [(1, 4), (1, 2)]
		result = collect_fractions(fractions)
		expected = (3, 4)

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()