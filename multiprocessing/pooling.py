import time
from functools import partial
from multiprocessing import Pool, current_process, cpu_count

def square_in_terms_of_addition(addition_component, x):
    """
        Purpose fully written in terms of cpu intensive operation
    """
    print(f"Running for {x} on {current_process()}")
    square = 0
    for _ in range(x):
        square += x
    return square + addition_component


start = time.perf_counter()
comparision_list = [10**8, 10**9, 10**8]

cpus = max(cpu_count() - 1, 1)

print("Number of cpus to be used: ", cpus)

addition_component = 2
partial_function = partial(square_in_terms_of_addition, addition_component)

# pool.map is defined as map(function, iterable)
# thus in cases where we want to pass multiple arguments to process function, we can make use of
# partial functions
# only the argument which we want as iterable should be used in map, like show below
# to be used in case of fixed components

with Pool(cpus) as mp_pool:
    results = mp_pool.map(partial_function, comparision_list)

print(results)

print(f"Everything took : {time.perf_counter() - start} seconds")