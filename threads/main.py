import time
from workers.squaredSum import SquaredSum
from workers.sleepyWorker import SleepyWorker

def main():
    calc_st = time.time()
    current_threads = []
    for i in range(5):
        max_time = (i+1)*100
        t = SquaredSum(max_time)
        current_threads.append(t)
    
    # blocks further execution untill all threads are resolved
    for t in current_threads:
        t.join()
    print(f"Calculating sum of squares took: {round(time.time() - calc_st, 1)}")


    current_threads = []
    sleep_st = time.time()
    for i in range(1, 11):
        t = SleepyWorker(i)
        current_threads.append(t)
    
    for t in current_threads:
        t.join()

    print(f"sleeping took: {round(time.time() - calc_st, 1)}")

if __name__ == "__main__":
    main()