import sys

from utils_for_polynomial import (
	parser,
	operators_extractor)

from polynomial import (
	Term,
	Polynomial
	)

def print_derivative(string=sys.argv[1]):
	parsed_strings_list = parser(string)
	operators_list = operators_extractor(string)
	terms_list = []

	for i in parsed_strings_list:
		terms_list.append(Term(i))

	poli = Polynomial(terms_list)

	derivatives_list = poli.derivative()

	solution = ''

	for index in range(len(derivatives_list)):
		solution += derivatives_list[index]
		if index != len(derivatives_list) - 1:
			solution += operators_list[index]

	if solution == '':
		solution = '0'

	return f"Derivative of f(x) = {string} is:\nf'(x) = {solution}"

def main():
	print(print_derivative())

if __name__ == '__main__':
	main()