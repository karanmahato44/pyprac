class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = self.first + '.' + self.last + '@company.com'

  def fullname(self):
    return f'{self.first} {self.last}'



class Developer(Employee):
  def __init__(self, first, last, pay, lang):
    super().__init__(first, last, pay)
    self.lang = lang




class Manager(Employee):
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    if employees is None:
      self.employees = []
    else:
      self.employees  = employees

  def add_emp(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)


  def remove_emp(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)


  def print_emp(self):
    for emp in self.employees:
      print('-->', emp.fullname())




dev1 = Developer('karan', 'mahato', 40000, 'python')
print(dev1.lang)

mgr1 = Manager('john', 'smith', 60000, [dev1])
print(mgr1.email)
mgr1.add_emp(dev1)
mgr1.print_emp()


print(isinstance(dev1, Employee))
print(isinstance(dev1, Developer))
print(isinstance(dev1, Manager))

print(issubclass(Developer, Employee))