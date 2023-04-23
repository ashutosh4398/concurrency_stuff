import time
from multiprocessing import Process


name = "Ashutosh"

def check_value_in_list(x):
    for i in range(10**8):
        i in x


def main():
    start_time = time.time()
    NUMBER_OF_PROCESSES = 4


    processes = []
    for _ in range(NUMBER_OF_PROCESSES):
        p = Process(target=check_value_in_list, args=([4,100, 20],))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    
    print(f"Execution took: {time.time() - start_time} seconds")

main()
