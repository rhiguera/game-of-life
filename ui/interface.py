from abc import ABC, abstractmethod

class BaseUI(ABC):
    @abstractmethod
    def __init__(self, grid):
        self.grid = grid

    @abstractmethod
    def run(self):
        """Starts the UI main loop."""
        pass

    @abstractmethod
    def update(self):
        """Updates the visual representation of the grid."""
        pass
