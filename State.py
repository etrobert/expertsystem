from enum import Enum

class State(Enum):
  TRUE = True
  FALSE = False
  UNKNOWN = 2

  def invert(self):
      if self == State.UNKNOWN:
        return State.UNKNOWN
      return State(not self.value)

  def __and__(self, operand):
    if self == State.UNKNOWN or operand == State.UNKNOWN:
      return State.UNKNOWN
    return State(self.value and operand.value)

  def __or__(self, operand):
    if self == State.FALSE and operand == State.FALSE:
      return State.FALSE
    if self == State.TRUE or operand == State.TRUE:
      return State.TRUE
    return State.UNKNOWN
