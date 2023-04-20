import threading
import functools

class SquaredSum(threading.Thread):
    def __init__(self, n, **kwargs) -> None:
        self._n = n
        super(SquaredSum, self).__init__(**kwargs)
        self.start()

    def _calculate_sum_of_squares(self):
        sum_squared = functools.reduce(lambda acc,x: acc + x**2, list(range(self._n)), 0)
        print("SUM OF SQUARES: ", sum_squared)
        

    def run(self):
        self._calculate_sum_of_squares()
