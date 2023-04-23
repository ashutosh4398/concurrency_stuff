import threading
import time

from utils import process_time

class Customer(threading.Thread):

    def __init__(self, name) -> None:
        super(Customer, self).__init__()
        self.name = name
        self.is_queued = False
        self.is_haircut_achieved = False

    def __str__(self) -> str:
        return self.name
    
    def visit(self, shop):
        print(f"{process_time()}:: {self.name} is entering the shop")
        self._shop = shop
        self.start()    

    def run(self):
        # while haircut is not achieved, keep visiting after few minutes
        while True:
            if self.is_haircut_achieved:
                break
            if not self.is_queued:
                with self._shop.lock:
                    if len(self._shop.waiting_queue) < self._shop.maximum_seats:
                        print(f"{process_time()}:: {self.name} is added to waiting")
                        self._shop.waiting_queue.append(self)
                        self.is_queued = True
                    else:
                        print(f"{process_time()}:: {self.name} will come after some time as queue is full")
                        time.sleep(5)
            
            time.sleep(1)
