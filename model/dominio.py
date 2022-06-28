class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somaDoisNumeros(self, num1, num2):
        if num1 + num2 >= 0 or num1 + num2 <= 0:
            return True
        else:
            return False

    def subtraiDoisNumeros(self, num1, num2):
        if num1 - num2 >= 0 or num1 + num2 <= 0:
            return True
        else:
            return False

    def multiplicaDoisNumeros(self, num1, num2):
        if num1 * num2 >= 0 or num1 * num2 <= 0:
            return True
        else:
            return False

    def divideDoisNumeros(self, num1, num2):
        if num2 != 0 and (num1 / num2 >= 0 or 0 >= num1 / num2):
            return True
        else:
            return False
