from dominio import *
import unittest


class MyTestCase(unittest.TestCase):

    def test_somaNumerosPositivos(self):
        calc = Calculadora(2, 2)
        calculo_soma = calc.somaDoisNumeros(2, 2)
        self.assertEqual(calculo_soma, True)

    def test_somaNumerosNegativos(self):
        calc = Calculadora(2, 2)
        calculo_soma_negativos = calc.somaDoisNumeros(-2, -2)
        self.assertEqual(calculo_soma_negativos, True)

    def test_subtraiNumerosPositivos(self):
        calc = Calculadora(2, 2)
        calculo_subtracao_positivos = calc.subtraiDoisNumeros(4, 2)
        self.assertEqual(calculo_subtracao_positivos, True)

    def test_subtraiNumerosNegativos(self):
        calc = Calculadora(2, 2)
        calculo_subtracao_negativos = calc.subtraiDoisNumeros(-2, -2)
        self.assertEqual(calculo_subtracao_negativos, True)

    def test_multiplicaNumerosPositivos(self):
        calc = Calculadora(2, 2)
        calculo_mult_positivos = calc.multiplicaDoisNumeros(2, 2)
        self.assertEqual(calculo_mult_positivos, True)

    def test_multiplicaNumerosNegativos(self):
        calc = Calculadora(2, 2)
        calculo_mult_negativos = calc.multiplicaDoisNumeros(-2, -2)
        self.assertEqual(calculo_mult_negativos, True)

    def test_divisaoPorZero(self):
        calc = Calculadora(2, 2)
        calculo_divisao_zero = calc.divideDoisNumeros(2, 0)
        self.assertEqual(calculo_divisao_zero, False)

    def test_divisaoNumerosPositivos(self):
        calc = Calculadora(2, 2)
        calculo_divisao_normal = calc.divideDoisNumeros(2, 1)
        self.assertEqual(calculo_divisao_normal, True)
