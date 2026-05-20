class Metrics:

    def __init__(self):

        self.comparisons = 0
        self.data_movements = 0
        self.execution_time = 0

    def reset(self):
        self.comparisons = 0
        self.data_movements = 0
        self.execution_time = 0