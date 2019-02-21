from Implication import Implication
from NamedProposition import NamedProposition
from System import System

class Parser:
  def __init__(self, text_input):
    self.text_input = text_input
  
  def parse(self):
      self.named_propositions = []
      self.propositions = \
        [self.parse_proposition(line) for line in self.text_input.splitlines()]
      return System(self.named_propositions, self.propositions)

  def parse_proposition(self, line):
      line = line.replace(' ', '')
      if line.find('=>') == -1:
        return self.get_named_proposition(line)
      split = line.split('=>')
      return Implication(self.get_named_proposition(split[0]), \
                         self.get_named_proposition(split[1]))

  def get_named_proposition(self, name):
      prop = next((p for p in self.named_propositions if p.name == name), None)
      if prop == None:
        prop = NamedProposition(name)
        self.named_propositions.append(prop)
      return prop
