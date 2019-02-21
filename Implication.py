from Proposition import Proposition
from State import State

class Implication(Proposition):
  def __init__(self, a:Proposition, b:Proposition):
    self.a = a
    self.b = b

  def get_state(self):
    if self.a.get_state() == State.FALSE or self.b.get_state() == State.TRUE:
      return State.TRUE
    if self.a.get_state() == State.TRUE and self.b.get_state() == State.FALSE:
      return State.FALSE
    return State.UNKNOWN

  def __repr__(self):
    return str(self.a) + ' => ' + str(self.b)
