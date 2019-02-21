from System import System
from Parser import Parser

with open('file', 'r') as f:
  s = Parser(f.read()).parse()
  s.solve()
  print('Input:')
  print(s.propositions)
  print('Result:')
  print(s.variables)
