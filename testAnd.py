from AndProposition import AndProposition
from NamedProposition import NamedProposition
from State import State

for a in list(State):
  for b in list(State):
    imp = AndProposition(NamedProposition('a', a), \
                      NamedProposition('b', b))
    print(str(a) + ' & ' + str(b) + ' = ' + str(imp.get_state()))
