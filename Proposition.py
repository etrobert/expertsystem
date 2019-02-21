from State import State
from abc import ABC, abstractmethod

class Proposition(ABC):
    @abstractmethod
    def get_state(self):
        pass
