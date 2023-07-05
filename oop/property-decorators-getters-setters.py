class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

    def __str__(self):
        return f'{self.first} {self.last}'


emp1 = Employee('john', 'smith', 40000)
Employee.first = 'jack'
print(emp1)
print(emp1.email)


emp1.fullname = 'Karan Mahato'
print(emp1)
print(emp1.email)

del emp1.fullname
print(emp1.email)
