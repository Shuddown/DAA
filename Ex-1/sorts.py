import math as m
from typing import Generator

import sys
import os
import matplotlib.pyplot as plt

# Get the directory of the current file
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from utils.random_test import test

def insertion_sort_helper(arr: list[int], start: int, step: int):
    for i in range(start + step, len(arr), step):
        key = arr[i]
        final_j = i
        for j in range(i - 1, start - 1, -1):  
            if arr[j] <= key:  
                break
            arr[j + step] = arr[j]  
            final_j -= step
        arr[final_j] = key  

def insertion_sort(arr: list[int]):
    insertion_sort_helper(arr, 0, 1)

def pratt_sequence(max_gap):
    """
    Generates the Pratt gap sequence up to max_gap.
    
    :param max_gap: The maximum gap value to generate.
    :return: A generator yielding the next gap in the Pratt sequence.
    """
    p = 0
    q = 0
    gap = 1
    while gap <= max_gap:
        yield gap
        p += 1
        gap = 2**p * 3**q
        if gap > max_gap:
            break
        q += 1
        gap = 2**p * 3**q


def shell_sort(arr: list[int], seq = pratt_sequence):
    sequence = seq(len(arr))
    for step in sequence:
       for start in range(step):
           insertion_sort_helper(arr, start, step)     
            
def radix_sort(arr: list[int], base: int = 256):
    
    def nth_digit(num: int, base: int, n: int):
        return (num //(base**n)) % base       
    
    
    def count_sort_helper(arr: list[int], base: int, n: int):
        counts = [0 for _ in range(base)]
        sorted_arr = [0 for _ in arr]
        for i in range(len(arr)):
            counts[nth_digit(arr[i], base, n)] += 1
        
        for i in range(1, base): counts[i] += counts[i-1]
        for i in range(len(arr) - 1, -1, -1):
            val = nth_digit(arr[i], base, n)
            counts[val] -= 1
            sorted_arr[counts[val]] = arr[i]
             
        for i in range(len(sorted_arr)):
            arr[i] = sorted_arr[i]     

    max_n = m.ceil(m.log(max(arr),base))
    for i in range(max_n): count_sort_helper(arr, base, i)


 
if __name__ == "__main__":
    ns = [10, 1000, 2000, 5000, 10000, 50000, 100000]
    test(radix_sort, ns, "log", "radix", "radix.png")
    test(insertion_sort, ns, "log", "insertion", "insertion.png")
    test(shell_sort, ns, "log", "shell", "shell.png")
    plt.show()
