#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import time, random

def max_elem(lst):
    if not lst:
        raise ValueError("Invalid input. List cannot be empty.")
    max_element = lst[0]
    for i in lst:
        if i >= max_element:
            max_element = i
    return max_element

def compute_time(l):
    t0 = time.perf_counter()
    result = 0
    try:
        result = max_elem(l)
    except ValueError as e:
        print(e)
    dt = time.perf_counter() - t0
    return result, dt

sizes = [10_000, 20_000, 40_000, 80_000, 160_000, 320_000, 640_000, 1_280_000]
for i in sizes:
    random_lst = [random.randint(0, 1_000_000) for _ in range(i)]
    result, spend_time = compute_time(random_lst)
    print(f"result: {result} | time: {spend_time}")
    del random_lst