import threading

from queue import Empty
from typing import List

from companies.models import Companies


class StorageScheduler(threading.Thread):

    def __init__(self, queue, **kwargs):
        self._queue = queue
        super(StorageScheduler, self).__init__(**kwargs)
        self.start()

    
    def run(self):
        while True:
            # val: List[str, int] = self._queue.get()
            # once empty list is received, quit thread
            # we will push empty list once yahooWorker puts "DONE" to mark end of process
            # if not val:
            #     break
            try:
                # if value is not received within 10 seconds, then terminate the thread
                val: List[str, int] = self._queue.get(timeout=10) 
            except Empty:
                break
            (symbol, price) = val

            sqliteWorker = SqliteWorker(symbol, price)
            print(f"{self.name} -> INSERTING VALUES IN DB: {val}")
            sqliteWorker.insert_in_db()
            


class SqliteWorker:

    def __init__(self, symbol, price) -> None:
        self.symbol = symbol or ""
        self.price = price or 0

    def insert_in_db(self):
        try:
            cmp = Companies.objects.get(symbol = self.symbol)
        except Companies.DoesNotExist:
            cmp = Companies()
        cmp.symbol = self.symbol
        cmp.price = self.price
        cmp.save()
