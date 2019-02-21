from System import System

with open('file', 'r') as f:
  s = System(f.read())
  print(s.propositions)
  s.solve()
  print(s.propositions)
