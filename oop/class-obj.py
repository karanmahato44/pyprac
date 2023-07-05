import datetime


class Employee:

    raise_amount = 1.04
    emp_no = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

        Employee.emp_no += 1

    def getfullname(self):
        return f'Full name: {self.first} {self.last}'

    def apply_raise(self):
        # self used so that't it can be used for individual raises
        self.pay = int(self.pay * self.raise_amount)

    # class methods

    @classmethod
    def set_raiseamt(cls, amount):
        cls.raise_amount = amount

    # using class method as an alternative constructor

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # same as return Employee(first, last, pay)
        return cls(first, last, pay)

    # static methods -> for those that operate on instance or class / doesn't take instance or class as first arg

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('karan', 'mahato', 40000)
emp2 = Employee('kyto', 'kappa', 0)
print(emp1.email)
print(emp2.email)
print(emp2.getfullname())

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(Employee.emp_no)


print('by calling the method on class: ', Employee.getfullname(emp1))


print(Employee.raise_amount)
Employee.set_raiseamt(2)
print(Employee.raise_amount)
print(emp1.apply_raise())
print(emp1.pay)


emp_new_str = 'john-doe-50000'

new_emp = Employee.from_string(emp_new_str)
print(new_emp.first)
print(new_emp.email)


my_date = datetime.date(2022, 2, 22)
print(f'is {my_date} a workday?: {Employee.is_workday(my_date)}')
