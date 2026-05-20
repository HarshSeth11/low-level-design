import time

from .base_strategy import BaseSortingStrategy 

class QuickSortStrategy(BaseSortingStrategy):
    def sort(self, data, metrics):
        start_time = time.time()

        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        sorted_left = self.sort(left, metrics)
        sorted_right = self.sort(right, metrics)

        metrics.execution_time = time.time() - start_time
        
        return sorted_left + middle + sorted_right
    