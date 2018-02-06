class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current

complex = Complex()
complex.create(1,2)

calculator = Calculator()
calculator.add(10)
calculator.add(20)

print(str(calculator.get_current()))