import unittest
from decimal import *
from silence import silence_exception, SilenceException
from precision import change_precision, ChangePrecision


class TestSilencerClass(unittest.TestCase):

    def test_class_silencing_of_passed_exception(self):
        exc = None

        try:
            with SilenceException(ValueError):
                raise ValueError
        except Exception as e:
            exc = e

        self.assertIsNone(exc)

    def test_class_silencing_of_passed_exception_w_message(self):
        with SilenceException(ValueError, 'Opa!'):
            raise ValueError('Opa!')

    def test_class_not_silencing_of_passed_exception_w_different_message(self):
        exc = None

        try:
            with SilenceException(ValueError, 'Opa!'):
                raise ValueError('Opi!')
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), 'Opi!')

    def test_func_silencing_of_passed_exception(self):
        exc = None

        try:
            with silence_exception(ValueError):
                raise ValueError
        except Exception as e:
            exc = e

        self.assertIsNone(exc)

    def test_func_silencing_of_passed_exception_w_message(self):
        with silence_exception(ValueError, 'Opa!'):
            raise ValueError('Opa!')

    def test_func_not_silencing_of_passed_exception_w_different_message(self):
        exc = None

        try:
            with silence_exception(ValueError, 'Opa!'):
                raise ValueError('Opi!')
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), 'Opi!')


class TestChangePrecisionFunction(unittest.TestCase):

    def test_adding_round_numbers_with_precision_of_3(self):

        with change_precision(3):
            result = Decimal(1.0000) + Decimal(1.00000)
            expected = Decimal('2.00')

        self.assertEqual(result, expected)

    def test_adding_not_round_numbers_with_precision_of_3(self):

        with change_precision(3):
            result = Decimal(1.2345) + Decimal(0.2345)
            expected = Decimal('1.47')

        self.assertEqual(result, expected)


class TestChangePrecisionClass(unittest.TestCase):

    def test_adding_round_numbers_with_precision_of_3(self):

        with ChangePrecision(3):
            result = Decimal(1.0000) + Decimal(1.00000)
            expected = Decimal('2.00')

        self.assertEqual(result, expected)

    def test_adding_not_round_numbers_with_precision_of_3(self):

        with ChangePrecision(3):
            result = Decimal(1.2345) + Decimal(0.2345)
            expected = Decimal('1.47')

        self.assertEqual(result, expected)

    def test_negative_number_precision(self):
        exc = None
        assrtion_msg = f'Precison must be a positive integer between 1 and {MAX_PREC}'

        try:
            with ChangePrecision(-3):
                pass
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), assrtion_msg)

    def test_cm_doesnt_change_prec_outside_with_block(self):
        with ChangePrecision(2):
            with_result = Decimal('1.123132132') + Decimal('2.23232')
            expected_with = Decimal('3.4')

        without_result = Decimal('1.123132132') + Decimal('2.23232')
        expected_without = Decimal('3.355452132')

        self.assertEqual(with_result, expected_with)
        self.assertEqual(without_result, expected_without)


if __name__ == '__main__':
    unittest.main()
