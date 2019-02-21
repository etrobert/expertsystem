from Proposition import Proposition
from State import State

class NamedProposition(Proposition):
  def __init__(self, name, state = State.UNKNOWN):
    self.name = name
    self.state = state

  def get_state(self):
    return self.state

  def __repr__(self):
    return self.name
