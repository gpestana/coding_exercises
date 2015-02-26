class Employee:
  nr_employees = 0

  def __init__(self, name):
    self.name = name
    Employee.nr_employees+=1

  def getName(self):
    return self.name

  def displayEmployees(self):
    print self.nr_employees
