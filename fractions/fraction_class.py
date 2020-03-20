class Fraction:

	def __init__(self, numerator, denominator):

		assert denominator >= 1, 'Denominator cannot be less than 1.'

		self.numerator = numerator
		self.denominator = denominator

	def __repr__(self):
		return f'Fraction {self}'

	def __str__(self):
		return f'{self.numerator}/{self.denominator}'

	def __eq__(self, other):
		return self.numerator == other.numerator and self.denominator == other.denominator

	def __lt__(self, other):
		return self.numerator / self.denominator < other.numerator / other.denominator

	def simplify(self):
		numerator = self.numerator
		denominator = self.denominator
		divisor = 2

		while divisor <= numerator:

			if numerator % divisor == 0 and denominator % divisor == 0:
				numerator = int(numerator/divisor)
				denominator = int(denominator/divisor)
				divisor = 2
			else:
				divisor +=1

		return Fraction(numerator, denominator)

	def __add__(self, other):

		numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
		denominator = self.denominator * other.denominator

		return Fraction(numerator, denominator).simplify()

def main():
	pass

if __name__ == '__main__':
	main()