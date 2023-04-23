import time
from functools import partial
from multiprocessing import Pool, current_process, cpu_count

def power_in_terms_of_addition(x, y):
    print(f"Running for {x} on {current_process()}")
    
    return x**y

start = time.perf_counter()

comparision_list = [10, 10, 10]
powers = [10, 9, 10]
cpus = max(cpu_count() - 1, 1)

print("Number of cpus to be used: ", cpus)


with Pool(cpus) as mp_pool:
    # starmap(square_in_terms_of_addition, [(10,8), (10,9), (10,10)])
    argument_list = [(x,y) for x,y in zip(comparision_list, powers)]
    results = mp_pool.starmap(power_in_terms_of_addition, argument_list)

print(results)

print(f"Everything took : {time.perf_counter() - start} seconds")
