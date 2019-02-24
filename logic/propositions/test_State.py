from logic.propositions.State import State
import unittest

class TestStateMethods(unittest.TestCase):
  def test_invert(self):
    self.assertEqual(State.TRUE.invert(), State.FALSE)
    self.assertEqual(State.FALSE.invert(), State.TRUE)
    self.assertEqual(State.UNKNOWN.invert(), State.UNKNOWN)

  def test_and(self):
    self.assertEqual(State.TRUE & State.TRUE, State.TRUE)
    self.assertEqual(State.TRUE & State.FALSE, State.FALSE)
    self.assertEqual(State.TRUE & State.UNKNOWN, State.UNKNOWN)
    self.assertEqual(State.FALSE & State.TRUE, State.FALSE)
    self.assertEqual(State.FALSE & State.FALSE, State.FALSE)
    self.assertEqual(State.FALSE & State.UNKNOWN, State.FALSE)
    self.assertEqual(State.UNKNOWN & State.TRUE, State.UNKNOWN)
    self.assertEqual(State.UNKNOWN & State.FALSE, State.FALSE)
    self.assertEqual(State.UNKNOWN & State.UNKNOWN, State.UNKNOWN)

  def test_or(self):
    self.assertEqual(State.TRUE | State.TRUE, State.TRUE)
    self.assertEqual(State.TRUE | State.FALSE, State.TRUE)
    self.assertEqual(State.TRUE | State.UNKNOWN, State.TRUE)
    self.assertEqual(State.FALSE | State.TRUE, State.TRUE)
    self.assertEqual(State.FALSE | State.FALSE, State.FALSE)
    self.assertEqual(State.FALSE | State.UNKNOWN, State.UNKNOWN)
    self.assertEqual(State.UNKNOWN | State.TRUE, State.TRUE)
    self.assertEqual(State.UNKNOWN | State.FALSE, State.UNKNOWN)
    self.assertEqual(State.UNKNOWN | State.UNKNOWN, State.UNKNOWN)

if __name__ == '__main__':
  unittest.main()
