import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 5) ==10

    def test_division(self):
        assert self.calc.division(self, 8, 4) ==2

    def test_substaction(self):
        assert self.calc.subtraction(self, 7, 6) ==1

    def test_adding(self):
        assert self.calc.adding(self, 3, 9) ==12


    def teardown(self):
        print('Выполнение метода Teardown')