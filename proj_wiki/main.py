# initializing django orm
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

import time

from multiprocessing import Queue

from workers import WikiWorker, YahooScheduler, YahooWorker, StorageScheduler



def thread_implementation():

    NUMBER_OF_WORKERS = 50
    NUMBER_OF_SQL_WORKERS = 50
    start = time.time()
    symbol_queue = Queue()
    output_queue = Queue()
    wiki = WikiWorker()


    current_threads = []
    for _ in range(NUMBER_OF_WORKERS):
        t = YahooScheduler(queue=symbol_queue, output_queues=[output_queue])
        current_threads.append(t)
    
    for i in range(NUMBER_OF_SQL_WORKERS):
        t = StorageScheduler(queue=output_queue, name=f"SQL_THREAD_{i+1}")
        current_threads.append(t)


    for symbol in wiki.extract_companies():
        symbol_queue.put(symbol)
        

    for _ in range(NUMBER_OF_WORKERS):
        symbol_queue.put("DONE")
    
    for t in current_threads:
        t.join()
    
    print(f"Total time: {round(time.time() - start, 1)} seconds")
    # Total time: 80.4 seconds

def sequential_implementation():

    wiki = WikiWorker()
    st = time.time()
    for symbol in wiki.extract_companies():
        yw = YahooWorker(symbol=symbol)
        price: float = yw.get_price()
        print(price)
    
    print(f"Total time: {round(time.time() - st, 1)} seconds")
    # Total time: 738.4 seconds

thread_implementation()
# sequential_implementation()
