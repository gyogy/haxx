import unittest
from my_sort import (
	my_sort,
	list_sorter,
	tuple_sorter,
	dict_sorter
	)	

class TestInput(unittest.TestCase):
	
	def test_input_of_non_iter_type(self):
		# ARRANGE
		iterable = 'a'
		exc = None

		# ACT
		try:
			my_sort(iterable)
		except Exception as err:
			exc = err

		# ASSERTS
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Please enter an iterable type.')

class TestListSorter(unittest.TestCase):

	def test_list_sorter_with_list_of_ints(self):
		# ARRANGE
		iterable = [5, 2, 98, 3245, 234, 654, 3]
		expected = [2, 3, 5, 98, 234, 654, 3245]
		
		# ACT
		result = list_sorter(iterable)

		# ASSERT
		self.assertEqual(result, expected)

	def test_list_sorter_descending(self):
		# ARRANGE
		iterable = [5, 2, 98, 3245, 234, 654, 3]
		expected = [3245, 654, 234, 98, 5, 3, 2]
		
		# ACT
		result = list_sorter(iterable, False)

		# ASSERT
		self.assertEqual(result, expected)

	def test_list_sorter_with_duplicate_values(self):
		# ARRANGE
		iterable = [1, 2, 3, 1, 2, 3, 1, 2, 3]
		expected = [1, 1, 1, 2, 2, 2, 3, 3, 3]
		
		# ACT
		result = list_sorter(iterable)

		# ASSERT
		self.assertEqual(result, expected)

class TestTupleSorter(unittest.TestCase):

	def test_tuple_sorter_with_tuple_of_ints(self):
		iterable = (4, 7, 2, 98, 324, 654, 8, 22, 54)
		expected = (2, 4, 7, 8, 22, 54, 98, 324, 654)

		result = tuple_sorter(iterable)

		self.assertEqual(result, expected)

	def test_tuple_sorter_descending(self):
		iterable = (4, 7, 2, 98, 324, 654, 8, 22, 54)
		expected = (654, 324, 98, 54, 22, 8, 7, 4, 2)

		result = tuple_sorter(iterable, False)

		self.assertEqual(result, expected)

class TestDictSorter(unittest.TestCase):

	def test_dict_sorter_with_valid_input(self):
		iterable = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'

		result = dict_sorter(iterable, key)
		expected = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

		self.assertEqual(result, expected)

	def test_dict_sorter_descending(self):
		iterable = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
		key = 'age'

		result = dict_sorter(iterable, key, False)
		expected = [{'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}]

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()