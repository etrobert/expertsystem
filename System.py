from Implication import Implication
from NamedProposition import NamedProposition
from State import State

class System:
  def __init__(self, text_input):
      self.propositions = \
        [self.parse_proposition(line) for line in text_input.splitlines()]

  def parse_proposition(self, line):
      line = line.replace(' ', '')
      split = line.split('=>')
      return Implication(NamedProposition(split[0]), NamedProposition(split[1]))
