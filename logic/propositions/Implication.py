from .Proposition import Proposition
from .State import State

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

  def update_states(self, my_state):
    if my_state == State.TRUE:
      if self.a.get_state() == State.TRUE:
        return self.b.update_states(State.TRUE)
      if self.b.get_state() == State.FALSE:
        return self.a.update_states(State.FALSE)
    if my_state == State.FALSE:
      return self.a.update_states(State.TRUE) + \
             self.b.update_states(State.FALSE)
    return 0

  def __repr__(self):
    return str(self.a) + ' => ' + str(self.b)
