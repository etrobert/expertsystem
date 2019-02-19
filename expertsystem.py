from system import system

with open('file', 'r') as f:
  s = system(f.read())
  print(s.states)
