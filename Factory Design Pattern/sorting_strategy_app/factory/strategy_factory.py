from strategies.bubble_sort import BubbleSortStrategy
from strategies.merge_sort import MergeSortStrategy
from strategies.insertion_sort import InsertionSortStrategy
from strategies.quick_sort import QuickSortStrategy


class StrategyFactory:

    @staticmethod
    def get_strategy(choice):

        strategies = {
            "1": BubbleSortStrategy,
            "2": MergeSortStrategy,
            "3": InsertionSortStrategy,
            "4": QuickSortStrategy
        }

        strategy_class = strategies.get(choice)

        if strategy_class:
            return strategy_class()

        return None