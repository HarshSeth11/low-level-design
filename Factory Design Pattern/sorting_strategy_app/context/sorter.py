
from utils.metrics import Metrics


class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

        self.metrics = Metrics()

    def set_strategy(self, strategy):
        self._strategy = strategy

        self.metrics.reset()

    def sort(self, data):
        return self._strategy.sort(data, self.metrics)