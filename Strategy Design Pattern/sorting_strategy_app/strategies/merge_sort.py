import time

from .base_strategy import BaseSortingStrategy


class MergeSortStrategy(BaseSortingStrategy):

    def sort(self, data, metrics):

        arr = data.copy()

        start_time = time.time()

        self._merge_sort(arr, 0, len(arr) - 1, metrics)

        metrics.execution_time = time.time() - start_time

        return arr

    def _merge_sort(self, data, low, high, metrics):

        if low < high:

            mid = (low + high) // 2

            self._merge_sort(data, low, mid, metrics)

            self._merge_sort(data, mid + 1, high, metrics)

            self._merge(data, low, mid, high, metrics)

    def _merge(self, data, low, mid, high, metrics):

        left = data[low:mid + 1]

        right = data[mid + 1:high + 1]

        i = 0
        j = 0
        k = low

        while i < len(left) and j < len(right):

            metrics.comparisons += 1

            if left[i] < right[j]:

                data[k] = left[i]

                i += 1

            else:

                data[k] = right[j]

                j += 1

            metrics.data_movements += 1

            k += 1

        while i < len(left):

            data[k] = left[i]

            metrics.data_movements += 1

            i += 1
            k += 1

        while j < len(right):

            data[k] = right[j]

            metrics.data_movements += 1

            j += 1
            k += 1