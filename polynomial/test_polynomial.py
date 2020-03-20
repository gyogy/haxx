import unittest
from utils_for_polynomial import parser
from polynomial import (
	Term,
	Polynomial
	)

class TestTermsClass(unittest.TestCase):

	def test_throwing_an_error_if_init_is_passed_something_other_than_string(self):
		string = []
		exc = None

		try:
			t = Term(string)
		except Exception as err:
			exc = err

		self.assertEqual(str(exc), f'Term\'s argument must be a string, not a {type(string)}') 

	def test_coefficient_and_power_assignment(self):
		string = '2x3'
		t = Term(string)

		self.assertEqual(t.coefficient, 2)
		self.assertEqual(t.power, 3)

	def test_derivate_returns_coefficient_only_when_x_raised_to_the_power_of_1(self):
		string = '2x'
		t = Term(string)

		result = t.derivate()
		expected = '2'

		self.assertEqual(result, expected)

	def test_derivate_with_a_full_term(self):
		string = '2x6'
		t = Term(string)

		result = t.derivate()
		expected = '12x^5'

		self.assertEqual(result, expected)

class TestPolymonialClass(unittest.TestCase):

	def test_derivative_function(self):
		parsed_strings_list = parser('2x^3 + 3x + 1')
		terms_list = []

		for i in parsed_strings_list:
			terms_list.append(Term(i))

		poli = Polynomial(terms_list)

		result = poli.derivative()
		expected = ['6x^2', '3']

		self.assertEqual(result, expected)

	def test_derivative_function_return_type(self):
		parsed_strings_list = parser('2x^3 + 3x + 1')
		terms_list = []

		for i in parsed_strings_list:
			terms_list.append(Term(i))

		poli = Polynomial(terms_list)

		result = type(poli.derivative())
		expected = list

		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()