from State import State

class Proposition:
  state = State.UNKNOWN
  def __init__(self, name, state = State.UNKNOWN):
    self.name = name
    self.state = state
  def __repr__(self):
    return self.name
