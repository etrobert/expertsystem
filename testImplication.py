from Implication import Implication
from State import State

for a in list(State):
  for b in list(State):
    print(str(a) + ' => ' + str(b) + ' = ' + str(Implication(a, b).state()))
