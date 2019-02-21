from System import System
from Parser import Parser
from ParseError import ParseError
import sys

def usage():
  print('usage: ' + sys.argv[0] + ' input_file')
  print('Your file should have newline separated logical propositions')
  print('Every operand and variable should be separated with a space')

if len(sys.argv) != 2:
  usage()
  sys.exit()
with open(sys.argv[1], 'r') as f:
  try:
    s = Parser(f.read()).parse()
  except ParseError as e:
    print('The given file has a format error: ' + str(e))
    usage()
    sys.exit()

  try:
    s.solve()
  except IncoherenceError as e:
    print('The given system has an incoherence : ' + str(e))

  print('System to solve:')
  print(s.propositions)
  print('Result:')
  for v in s.variables:
    print(v.name + ': ' + str(v.state))
