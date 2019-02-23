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
    if self == State.TRUE and operand == State.TRUE:
      return State.TRUE
    if self == State.FALSE or operand == State.FALSE:
      return State.FALSE
    return State.UNKNOWN

  def __or__(self, operand):
    if self == State.FALSE and operand == State.FALSE:
      return State.FALSE
    if self == State.TRUE or operand == State.TRUE:
      return State.TRUE
    return State.UNKNOWN
