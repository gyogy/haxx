from simplify_fraction import simplify_fraction

def sum_normalized_fractions(frac1, frac2):
	
	nom1 = frac1[0]
	nom2 = frac2[0]
	denom = frac1[1]

	summa = nom1 + nom2, denom 

	return tuple(summa)

def normalize_fractions(fractions):
	
	first_fraction = fractions[0]
	second_fraction = fractions[1]

	normalized_denominator = int(
		first_fraction[1] * second_fraction[1]
		)

	first_normalized_nominator = int(
		first_fraction[0] * second_fraction[1]
		)

	second_normalized_nominator = int(
		second_fraction[0] * first_fraction[1]
		)

	normalized_fractions = [
		(first_normalized_nominator, normalized_denominator), 
		(second_normalized_nominator, normalized_denominator)
		]

	return normalized_fractions


def collect_fractions(fractions):
	
	frac1 = normalize_fractions(fractions)[0]
	frac2 = normalize_fractions(fractions)[1]

	summa = sum_normalized_fractions(frac1, frac2)

	return simplify_fraction(summa)

def main():
	pass

if __name__ == '__main__':
	main()