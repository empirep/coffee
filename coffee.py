from tabulate import tabulate

class coffeeMachine(object):
   def __init__(self, machine, serving):
      self.machine = machine
      self.serving = serving
      self.taste = None
      self.maintenance = 0.0
   def nCost(self, n):
      return self.machine + (self.serving * n)

class dripCoffeeMachine(coffeeMachine):
   def __init__(self, filename=None):
      super(dripCoffeeMachine, self).__init__()
      self["name"] = filename

class espressoMachine(coffeeMachine):
    pass

class podEspressoMachine(espressoMachine):
    pass

class automaticEspressoMachine(espressoMachine):
    pass

mrCoffee = dripCoffeeMachine(30, 0.42)
nespresso = podEspressoMachine(100, 0.60)
jura = automaticEspressoMachine(600, mrCoffee.serving / 2)

cost_matrix = []
cost_matrix_columns = ['n', 'Mr Coffee', 'Nespresso', 'Jura']
data_interval = 100
data_points = 30

for i in range(1, data_points + 1):
    n = i * data_interval
    cost_matrix.append([n, mrCoffee.nCost(n), nespresso.nCost(n), jura.nCost(n)])

print(tabulate(cost_matrix, headers=cost_matrix_columns))
