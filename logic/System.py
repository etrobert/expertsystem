from .propositions.State import State

class System:
  def __init__(self, variables, propositions):
      self.variables = variables
      self.propositions = propositions

  def solve(self):
      updates = 1
      while updates > 0:
        updates = 0
        for proposition in self.propositions:
          updates += proposition.update_states(State.TRUE);
