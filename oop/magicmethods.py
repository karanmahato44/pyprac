class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    # def __repr__(self):
    #   return f'Employee({self.first} {self.last} {self.pay})'

    def __str__(self):
        return f'{self.fullname()}'

    def __add__(self, other):
        return f'{self.pay + other.pay}'


emp1 = Employee('foo', 'bar', 10000)
emp2 = Employee('lorem', 'ipsum', 20000)

print(emp1)
print(emp2)
print(emp1 + emp2)
