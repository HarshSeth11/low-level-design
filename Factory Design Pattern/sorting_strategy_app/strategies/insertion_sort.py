import time
from .base_strategy import BaseSortingStrategy

class InsertionSortStrategy(BaseSortingStrategy):
    def sort(self, data, metrics):
        start_time = time.time()

        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
                metrics.comparisons += 1
                metrics.data_movements += 1
            data[j + 1] = key

        metrics.execution_time = time.time() - start_time
        return data
    