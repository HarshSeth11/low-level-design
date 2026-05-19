from strategies.bubble_sort import BubbleSortStrategy
from strategies.merge_sort import MergeSortStrategy
from strategies.insertion_sort import InsertionSortStrategy
from strategies.quick_sort import QuickSortStrategy

from context.sorter import Sorter


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


def main():

    while True:

        print("\nChoose Sorting Algorithm:")
        print("1. Bubble Sort")
        print("2. Merge Sort")
        print("3. Insertion Sort")
        print("4. Quick Sort")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "5":
            print("\nExiting Application...")
            break

        strategy = get_strategy(choice)

        if strategy is None:
            print("\nInvalid Choice. Please try again.")
            continue

        try:

            data = list(
                map(
                    int,
                    input("\nEnter numbers separated by space: ").split()
                )
            )

        except ValueError:

            print("\nInvalid Input. Please enter only integers.")
            continue

        sorter = Sorter(strategy)

        sorted_data = sorter.sort(data)

        print("\nSorted Data:", sorted_data)

        print("\nMetrics:")
        print("Comparisons:", sorter.metrics.comparisons)
        print("Data Movements:", sorter.metrics.data_movements)
        print(f"Execution Time: {sorter.metrics.execution_time:.6f} sec")


if __name__ == "__main__":
    main()