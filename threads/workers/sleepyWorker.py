import threading
import time

class SleepyWorker(threading.Thread):
    def __init__(self, seconds, **kwargs):
        self._seconds = seconds
        super(SleepyWorker, self).__init__(**kwargs)
        # start the thread execution as soon as it is initialized
        self.start()
    
    def __sleep_a_little(self):
        time.sleep(self._seconds)
        print(f"Slept for {self._seconds} seconds")
    
    def run(self):
        self.__sleep_a_little()