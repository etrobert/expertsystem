from Implication import Implication
from NamedProposition import NamedProposition
from State import State

for a in list(State):
  for b in list(State):
    imp = Implication(NamedProposition('a', a), \
                      NamedProposition('b', b))
    print(str(a) + ' => ' + str(b) + ' = ' + str(imp.get_state()))
