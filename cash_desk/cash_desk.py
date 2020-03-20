class Bill():

	def __init__(self, amount):
		
		if type(amount) is not int:
			raise TypeError(f'Amount must be an integer, but is an {type(amount)}.')

		if amount < 0:
			raise ValueError('Amount cannot be a negative number.')

		self.amount = amount

	def __str__(self):
		return f'A ${self.amount} bill'

	def __repr__(self):
		return f'A ${self.amount} bill'

	def __int__(self):
		return int(self.amount)

	def __eq__(self, other):
		return self.amount == other.amount

	def __hash__(self):
		return self.amount

class BatchBill():
	def __init__(self, bills):

		for bill in bills:
			if type(bill) != Bill:
				raise TypeError('All list elements must be an instance of the Bill class.')
		
		self.bills = bills

	def __getitem__(self, index):
		return self.bills[index]

	def __len__(self):
		return len(self.bills)

	def total(self):
		summa = 0

		for i in self.bills:
			summa += int(i)

		return summa

class CashDesk():
	def __init__(self):
		self.cash_desk = {}

	def take_money(self, money):

		if type(money)  == Bill:
			if money in self.cash_desk:
				self.cash_desk[money] += 1
			else:
				self.cash_desk[money] = 1

		elif type(money)  == BatchBill:
			for bill in money:
				if bill in self.cash_desk:
					self.cash_desk[bill] += 1
				else:
					self.cash_desk[bill] = 1

	def total(self):
		total = 0

		for i in self.cash_desk:
			total += int(i) * self.cash_desk[i]

		return total

	def inspect(self):
		print(f'We have a total of ${self.total()} in the cash desk.')
		print('We have the following count of bills, sorted in ascending order:')
		for i in self.cash_desk:
			print(i,'-', self.cash_desk[i])

def main():
	values = [10, 20, 50, 100, 100, 100]
	bills = [Bill(value) for value in values]

	batch = BatchBill(bills)

	desk = CashDesk()
	desk.take_money(batch)
	desk.take_money(Bill(10))

	desk.inspect()

if __name__ == '__main__':
	main()