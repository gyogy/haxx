import unittest
from sort_fractions import (
	get_key,
	normalize_fractions,
	sort_norm_fractions,
	denormalize_sorted_fractions
	)

class TestGetKey(unittest.TestCase):
	
	def test_random_fractions(self):
		noms = [2, 22, 6, 3]
		denoms = [3, 7, 8, 5]

		result = get_key(noms, denoms)
		expected = [[7, 8, 5], [3, 8, 5], [3, 7, 5], [3, 7, 8]]

		self.assertEqual(result, expected)

class TestNormalizeFractions(unittest.TestCase):

	def test_example_fractions(self):
		noms = [2, 22, 6, 3]
		denoms = [3, 7, 8, 5]
		key = [[7, 8, 5], [3, 8, 5], [3, 7, 5], [3, 7, 8]]

		expected = [(560, 840), (2640, 840), (630, 840), (504, 840)]
		result = normalize_fractions(noms, denoms, key)

		self.assertEqual(result, expected)

	def test_normalize_list_of_fractions_with_some_equal_elements(self):
		noms = [2, 4, 6, 3]
		denoms = [3, 6, 8, 5]
		key = [[6, 8, 5], [3, 8, 5], [3, 6, 5], [3, 6, 8]]

		expected = [(480, 720), (480, 720), (540, 720), (432, 720)]
		result = normalize_fractions(noms, denoms, key)

		self.assertEqual(result, expected)

class TestSortNormalizedFractions(unittest.TestCase):

	def test_example_norm_fractions(self):

		key = [[7, 8, 5], [3, 8, 5], [3, 7, 5], [3, 7, 8]]
		fractions = [(560, 840), (2640, 840), (630, 840), (504, 840)]
		expected = [(504, 840), (560, 840), (630, 840), (2640, 840)]
		result = sort_norm_fractions(fractions, key)

		self.assertEqual(result[0], expected)

	def test_key_sorting(self):

		key = [[7, 8, 5], [3, 8, 5], [3, 7, 5], [3, 7, 8]]
		fractions = [(560, 840), (2640, 840), (630, 840), (504, 840)]
		expected = [[3, 7, 8], [7, 8, 5], [3, 7, 5], [3, 8, 5]]
		result = sort_norm_fractions(fractions, key)

		self.assertEqual(result[1], expected)

class TestDenormalizeSortedFractions(unittest.TestCase):

	def test_example_sorted_fractions(self):
		
		key = [[3, 7, 8], [7, 8, 5], [3, 7, 5], [3, 8, 5]]
		fractions = [(504, 840), (560, 840), (630, 840), (2640, 840)]
		result = denormalize_sorted_fractions(fractions, key)
		expected = [(3, 5), (2, 3), (6, 8), (22, 7)]

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()