from State import State
from abc import ABC, abstractmethod

class Proposition(ABC):
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def update_states(self, my_state):
        pass

    @abstractmethod
    def __repr__(self):
        pass
