from Implication import Implication
from AndProposition import AndProposition
from OrProposition import OrProposition
from NamedProposition import NamedProposition
from System import System
from ParseError import ParseError
import re

class Parser:
  priority = {'=>': 0, '<=': 0, '<=>': 0, '|': 1, '&': 2}
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
      if op == '<=':
        return Implication(b, a)
      if op == '<=>':
        return AndProposition(Implication(a, b), Implication(b, a))
      if op == '&':
        return AndProposition(a, b)
      if op == '|':
        return OrProposition(a, b)

  def parse_proposition(self, line):
      line = re.sub('\s+', ' ', line).strip()
      items = line.split(' ')
      items.reverse()

      a = self.get_named_proposition(items.pop())
      if not items:
        return a
      op = items.pop()
      if not op in self.priority:
        raise ParseError('Unknown operand: ' + op)
      return self.parse_items(a, op, items)

  def parse_items(self, a, op, items):
      b = self.get_named_proposition(items.pop())
      if not items:
        return self.create_proposition(a, op, b)
      next_op = items.pop()
      if not next_op in self.priority:
        raise ParseError('Unknown operand: ' + op)
      if self.priority[op] > self.priority[next_op]:
        return self.parse_items(self.create_proposition(a, op, b), next_op, items)
      return self.create_proposition(a, op, self.parse_items(b, next_op, items))

  def get_named_proposition(self, name):
      prop = next((p for p in self.named_propositions if p.name == name), None)
      if prop == None:
        prop = NamedProposition(name)
        self.named_propositions.append(prop)
      return prop
