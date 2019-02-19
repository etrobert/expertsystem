from State import State
from abc import ABC, abstractmethod

class Proposition(ABC):
    @abstractmethod
    def state(self):
        pass
