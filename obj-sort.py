class employee():
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def __repr__(self):
      return f'{self.name} {self.age} {self.salary}'



e1 = employee('lorem', '22', '44000')
e2 = employee('ipsum', '44', '66000')
e3 = employee('foo', '25', '50000')
e4 = employee('bar', '20', '40000')

employees = [e1, e2, e3, e4]

# def e_sort(emp):
#   return emp.name

sorted_emp = sorted(employees, key=lambda e: e.name)

# use attrgetter
# from operator import attrgetter
# sorted_emp = sorted(employees, key=attrgetter('name'))


print(sorted_emp)