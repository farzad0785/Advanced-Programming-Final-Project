#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

from random import randint
import time

def buble_sort(lst):
    if not lst:
        raise ValueError("Invalid list. List cannot be empty. ")

    for i in range(len(lst)):
        #flag for checking swaps
        swapped = False
        for j in range(1, len(lst) - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                swapped = True

        #if there isn't any swap, then the list is already sorted.
        if not swapped:
            break
    return lst
def compute_time(lst):
    t0 = time.perf_counter()
    result = 0
    try:
        result = buble_sort(lst)
    except ValueError as e:
        print(e)
    dt = time.perf_counter() - t0
    return result, dt
sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
for size in sizes:
    test_list = [randint(1, 10000) for _ in range(size)]
    answer, spend_time = compute_time(test_list)
    print(f"result: {answer} | spend time: {spend_time}")