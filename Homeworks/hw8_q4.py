#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import time, random

def duplicate_elem(lst):
    if not lst:
        raise ValueError("Invalid input. List cannot be empty.")
    counter = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                counter += 1
    return counter

def compute_time(lst):
    t0 = time.perf_counter()
    result = 0
    try:
        result = duplicate_elem(lst)
    except ValueError as e:
        print(e)
    dt = time.perf_counter() - t0
    return result, dt

sizes = [500, 1000, 2000, 4000, 8000, 16000]
for i in sizes:
    random_lst = [random.randint(1,10_000) for _ in range(i)]
    result, spend_time = compute_time(random_lst)
    print(f"result: {result} | spend time: {spend_time}")
    del random_lst