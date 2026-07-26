#Name: Aliasghar Rashidabadi
#Student ID: 40419533
#Course: Advanced Programming

import time

def division_2(n):
    if n <= 0:
        raise ValueError("Enter positive integer. ")
    counter = 0
    while n > 1:
        n //= 2
        counter += 1
    return counter

def compute_time(n):
    t0 = time.perf_counter()
    result = 0
    try:
        result = division_2(n)
    except ValueError as e:
        print(e)
    dt = time.perf_counter() - t0
    return result, dt

numbers_list = [16, 32, 64, 128, 256, 512, 1_024, 2**20, 2**40, 2**60, 2**80, 2**100]
for i in numbers_list:
    result, spend_time = compute_time(i)
    print(f"result: {result} | spend time: {spend_time}")