import unittest
from cash_desk import (
	Bill,
	BatchBill,
	CashDesk
	)

class TestBill(unittest.TestCase):

	def test_raising_of_type_error_for_amount_type_different_than_int(self):

		exc = None

		try:
			amount = []
			Bill(amount)
		except Exception as err:
			exc = err

		self.assertEqual(str(exc), f'Amount must be an integer, but is an {type(amount)}.')

	def test_raising_of_value_error_for_negative_bill_amount(self):

		exc = None

		try:
			Bill(-3)
		except Exception as err:
			exc = err

		self.assertEqual(str(exc), 'Amount cannot be a negative number.')

	def test_str(self):
		a = Bill(10)

		self.assertEqual(repr(a), f'A ${a.amount} bill')

	def test_int(self):
		a = Bill(10)

		self.assertEqual(int(a), 10)

	def test_hash_with_bills_of_the_same_amount(self):
		a = Bill(10)
		b = Bill(10)

		self.assertEqual(hash(a), hash(b))

	def test_hash_with_bills_of_different_amounts(self):
		a = Bill(10)
		b = Bill(3)

		self.assertNotEqual(hash(a), hash(b))

class TestBatchBill(unittest.TestCase):

	def test_raises_type_error_if_bills_is_not_a_list_of_bill_instances(self):
		bills = [Bill(1), 10, 'a']

		exc = None

		try:
			BatchBill(bills)
		except TypeError as err:
			exc = err

		self.assertEqual(str(exc), 'All list elements must be an instance of the Bill class.')

	def test_getitem(self):
		values = [1, 2, 5, 10]
		bills = [Bill(value) for value in values]

		batch = BatchBill(bills)

		result = str(batch[3])
		expected = 'A $10 bill'

		self.assertEqual(result, expected)

	def test_showing_batch_lenght(self):
		values = [1, 2, 5, 10]
		bills = [Bill(value) for value in values]

		batch = BatchBill(bills)

		result = len(batch)
		expected = 4

		self.assertEqual(result, expected)

	def test_showing_total_amount_in_batch(self):
		values = [1, 2, 5, 10]
		bills = [Bill(value) for value in values]

		batch = BatchBill(bills)

		result = batch.total()
		expected = 18

		self.assertEqual(result, expected)

class TestCashDesk(unittest.TestCase):

	def test_take_money_with_a_single_bill(self):
		b = Bill(10)
		
		desk = CashDesk()
		desk.take_money(b)

		result = desk.cash_desk

		expected = {b: 1}

		self.assertEqual(result, expected)

	def test_take_money_with_a_batch_bill(self):
		values = [10, 20, 50, 100, 100, 100]
		bills = [Bill(value) for value in values]
		batch = BatchBill(bills)

		desk = CashDesk()
		desk.take_money(batch)

		result = desk.cash_desk

		expected = {bills[0]:1, bills[1]:1,bills[2]:1,bills[3]:3}

		self.assertEqual(result, expected)

	def test_checking_total(self):
		values = [10, 20, 50, 100, 100, 100]
		bills = [Bill(value) for value in values]
		batch = BatchBill(bills)

		desk = CashDesk()
		desk.take_money(batch)
		desk.take_money(Bill(10))

		result = desk.total()

		expected = 390

if __name__ == '__main__':
	unittest.main()