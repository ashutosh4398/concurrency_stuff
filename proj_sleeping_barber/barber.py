import threading
import time

from utils import process_time


class Barber(threading.Thread):

    def __init__(self, waiting_queue, lock, **kwargs):
        super(Barber, self).__init__(**kwargs)
        self.waiting_queue = waiting_queue
        self.lock = lock
        self.status = None
        self.current_customer = None
        self.start()

    def _process_customer(self, customer):
        self.current_customer = customer
        print(f"{process_time()}:: Processing customer: {customer.name}")
        time.sleep(5)
        customer.is_haircut_achieved = True
        print(f"{process_time()}:: Processed customer: {customer.name}")
        self.current_customer = None
    
    def sleep(self):
        print(f"{process_time()}:: Sleeping...")
        time.sleep(1)

    def run(self):
        while True:
            with self.lock:
                if self.current_customer:
                    pass
                elif self.waiting_queue:
                    customer = self.waiting_queue[0]
                    del self.waiting_queue[0]
                    self._process_customer(customer)
                else:
                    self.sleep()
            time.sleep(0.2)
                    
                