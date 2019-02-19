from Proposition import Proposition
from State import State

class System:
  # propositions is of type [Proposition]
  states = {'A': State.UNKNOWN, 'B': State.TRUE}
  
  def __init__(self, text_input):
      for line in text_input.splitlines():
        self.parse_line(line)

  def find_prop(self, name):
      return [prop for prop in self.propositions if prop.name == name]

  def parse_line(self, line):
      line = line.replace(' ', '')
      split = line.split('=>')
      if split[0] in self.states and self.states[split[0]] == State.TRUE:
        if self.states[split[1]] == State.FALSE:
          raise Exception('Incoherence')
        self.states[split[1]] = State.TRUE
      if split[0] not in self.states:
        self.states[split[0]] = State.UNKNOWN
      if split[1] not in self.states:
        self.states[split[1]] = State.UNKNOWN
