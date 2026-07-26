#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import time, random

def first_elem(lst):
    if not lst:
        raise ValueError("Invalid input. List cannot be empty")
    return lst[0]

def compute_time(lst):
    t0 = time.perf_counter()
    result = 0
    try:
        result = first_elem(lst)
    except ValueError as e:
        print(e)
    dt = time.perf_counter() - t0
    return result, dt

sizes = [100, 1_000, 10_000, 100_000, 1_000_000, 100_000_000]
for i in sizes:
    random_lst = [random.randint(1, 1_000_000) for _ in range(i)]
    result, spend_time = compute_time(random_lst)
    print(f"result: {result} | time: {spend_time}")
    del random_lst