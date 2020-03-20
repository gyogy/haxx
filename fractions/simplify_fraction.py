def simplify_fraction(fraction):

	nominator = fraction[0]
	denominator = fraction[1]
	divisor = 2

	while divisor <= nominator:

		if nominator % divisor == 0 and denominator % divisor == 0:
			nominator = int(nominator/divisor)
			denominator = int(denominator/divisor)
			divisor = 2
		else:
			divisor +=1

	return (nominator, denominator)

def main():
	pass

if __name__ == '__main__':
	main()