import os
import sys
# Get the directory of the current file
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)
from utils.random_test import unique_rand
import time

def binary_search_iterative(arr: list[int], key: int) -> int:
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        check_val = arr[mid]
        if (key < check_val): right = mid - 1
        elif (key > check_val): left = mid + 1
        else: return mid
    return -1

def binary_search_recursive(arr: list[int], key: int) -> int:
    if(len(arr) == 0):
        return -1
    
    if(len(arr) == 1 and arr[0] == key):
        return 0
    
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    check_val = arr[mid]
    if (key < check_val): return binary_search_recursive(arr[:mid], key)
    if (key > check_val):
        result = binary_search_recursive(arr[mid+1:], key)
        return -1 if result == -1 else result + mid + 1
    return mid

if __name__ == "__main__":
    n = 100000
    start_time = time.perf_counter()
    binary_search_iterative(unique_rand(n), 1)
    end_time = time.perf_counter()
    print(f"Iterative: {end_time - start_time}")
    start_time = time.perf_counter()
    binary_search_recursive(unique_rand(n), 1)
    end_time = time.perf_counter()
    print(f"Recursive: {end_time - start_time}")
