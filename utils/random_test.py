import random as rn
import time
import matplotlib.pyplot as plt
import numpy as np

def unique_rand(n: int) -> list[int]:
    rands = list(range(n))
    rn.shuffle(rands)
    return rands

def test(func, n_vals, scale, func_name, save_path):
    times = []
    for n in n_vals:
        prelims = []
        for i in range(1):
            arr = unique_rand(n)
            start = time.perf_counter()
            func(arr)
            time_taken = time.perf_counter() - start
            prelims.append(time_taken)
        times.append(np.mean(prelims))
    plt.plot(n_vals, times, 'o-', label = func_name)
    plt.legend()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.ylabel("Time (s)")
    plt.xlabel("N-value")
    plt.savefig(save_path)
    return times
    
if __name__ == "__main__":
    test(sorted, [i for i in range(100, 10000, 100)], "log", "sort", "1.png")