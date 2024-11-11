import unittest
from calculator import calculator


class TestCalculator(unittest.TestCase):
    def test_operation_none(self):
        with self.assertRaises(Exception) as ex:
            calculator(None, 2, 2)
        self.assertEqual(ex.exception.args[0], 'Operacao nao pode ser nulo')

    def test_invalid_numbers(self):
        with self.assertRaises(Exception) as ex:
            calculator('add', None, 2)
        self.assertEqual(ex.exception.args[0], 'Informe dois numeros validos para realizar a operacao')
        with self.assertRaises(Exception) as ex2:
            calculator('add', 2, None)
        self.assertEqual(ex.exception.args[0], 'Informe dois numeros validos para realizar a operacao')
                         
    def test_is_operation_valid(self):
        with self.assertRaises(Exception) as ex:
            calculator('fatorial', 10, 2)
        self.assertEqual(ex.exception.args[0], 'informe uma operacao valida (add, sub, mult, div)')

    def test_sum(self):
        result = calculator('add', 10, 30)
        self.assertEqual(result, 40)

    def test_sub(self):
        result = calculator('sub', 50, 25)
        self.assertEqual(result, 25)

    def test_mult(self):
        result = calculator('mult', 2, 5)
        self.assertEqual(result, 10)
    
    def test_div(self):
        result = calculator('div', 10, 5)
        self.assertEqual(result, 2)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError) as ze:
            calculator('div', 10, 0)
        self.assertEqual(ze.exception.args[0], 'Voce nao pode dividir um numero por 0')

if __name__ == '__main__':
    unittest.main()