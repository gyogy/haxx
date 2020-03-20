def operators_extractor(string):

	operators_list = []

	for char in string:

		if char == '+' or char == '-':
			operators_list.append(char)

	return operators_list

def parser(string):

	terms_list = []

	for i in string.split('-'):

		for j in i.split('+'):

			terms_list.append(j.strip())

	for k in range(len(terms_list)):

			terms_list[k] = terms_list[k].replace('^', '')
			terms_list[k] = terms_list[k].replace('*', '')

	return terms_list

def main():
	print(parser('2x^3 - 6*x^2 + 5'))


if __name__ == '__main__':
	main()