#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

from random import randint
import time

def merge_sort(lst):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = len(lst)//2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j= 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j += 1

    while i< len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def compute_time(lst):
    t0 = time.perf_counter()
    result = 0
    try:
        result = merge_sort(lst)
    except ValueError as e:
        print(e)
    dt = time.perf_counter() - t0
    return result, dt

sizes = [10, 100, 500, 1000, 2000, 5000, 10000]
for size in sizes:
    random_lst = [randint(1,10_000) for _ in range(size)]
    result, spend_time = compute_time(random_lst)
    print(f"result: {result} | spend time: {spend_time}")