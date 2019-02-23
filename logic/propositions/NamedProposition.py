from .Proposition import Proposition
from .State import State
from ..IncoherenceError import IncoherenceError

class NamedProposition(Proposition):
  def __init__(self, name, state = State.UNKNOWN):
    self.name = name
    self.state = state

  def get_state(self):
    return self.state

  def update_states(self, my_state):
    if self.state == State.UNKNOWN:
      self.state = my_state
      return 1
    if self.state != my_state:
      raise IncoherenceError(self.name)
    return 0

  def __repr__(self):
    return self.name
