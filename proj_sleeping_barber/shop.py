
class Shop():
    
    def __init__(self, lock, waiting_queue=[], max_seats = 5, **kwargs) -> None:
        self.waiting_queue = waiting_queue
        self.maximum_seats = max_seats
        self.lock = lock
        self.round_robin = []