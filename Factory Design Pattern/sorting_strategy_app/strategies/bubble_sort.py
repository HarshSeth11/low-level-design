import time

from .base_strategy import BaseSortingStrategy

class BubbleSortStrategy(BaseSortingStrategy):
    def sort(self, data, metrics):
        n = len(data)
        start_time = time.time()
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    metrics.data_movements += 1
                metrics.comparisons += 1
        
        metrics.execution_time = time.time() - start_time
        return data