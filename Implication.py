from Proposition import Proposition
from State import State

class Implication(Proposition):
  def __init__(self, a:Proposition, b:Proposition):
    self.a = a
    self.b = b

  def get_state(self):
    if self.a == State.FALSE or self.b == State.TRUE:
      return State.TRUE
    if self.a == State.TRUE and self.b == State.FALSE:
      return State.FALSE
    return State.UNKNOWN

  def __repr__(self):
    return str(self.a) + ' => ' + str(self.b)
