from Implication import Implication
from NamedProposition import NamedProposition
from System import System
from ParseError import ParseError

class Parser:
  priority = {'=>': 1}
  def __init__(self, text_input):
    self.text_input = text_input
  
  def parse(self):
      self.named_propositions = []
      self.propositions = []
      for line in self.text_input.splitlines():
          try:
            self.propositions.append(self.parse_proposition(line))
          except IndexError:
            raise ParseError('Incorrect line: "' + line + '"')
      return System(self.named_propositions, self.propositions)

  def create_proposition(self, a, op, b):
      if op == '=>':
        return Implication(a, b)
      raise ParseError('Unknown operand: ' + op)

  def parse_proposition(self, line):
      items = line.split(' ')
      items.reverse()

      a = self.get_named_proposition(items.pop())
      if not items:
        return a
      op = items.pop()
      return self.parse_items(a, op, items)

  def parse_items(self, a, op, items):
      b = self.get_named_proposition(items.pop())
      if not items:
        return self.create_proposition(a, op, b)
      next_op = items.pop()
      if self.priority[op] > self.priority[next_op]:
        return self.parse_items(self.create_proposition(a, op, b), next_op, items)
      return self.create_proposition(a, op, self.parse_items(b, next_op, items))

  def get_named_proposition(self, name):
      prop = next((p for p in self.named_propositions if p.name == name), None)
      if prop == None:
        prop = NamedProposition(name)
        self.named_propositions.append(prop)
      return prop
