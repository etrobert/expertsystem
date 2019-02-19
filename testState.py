from State import State

for a in list(State):
  for b in list(State):
    print(str(a) + ' & ' + str(b) + ' = ' + str(a & b))

print('\n')

for a in list(State):
  for b in list(State):
    print(str(a) + ' | ' + str(b) + ' = ' + str(a | b))

print('\n')

for a in list(State):
  print ('not ' + str(a) + ' = ' + str(a.invert()))
