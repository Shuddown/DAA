from random import randint
from math import sqrt
from typing import Callable
from time import perf_counter
import matplotlib.pyplot as plt
class Item:
    
    def __init__(self, value, weight) -> None:
        self.v = value
        self.w = weight
    
    def __repr__(self):
        return f"(v:{self.v}, w:{self.w})"

    
    def __str__(self):
        return f"(v:{self.v}, w:{self.w})"


table_0 = {}
def dynamic_knapsack(items: list[Item], W: int)-> int:
    global table_0
    if(items == []): return 0
    if(W == 0): return 0
    n = len(items)
    curr = (n-1, W)
    if curr in table_0: return table_0[curr]
    
    if W - items[n-1].w >= 0: 
        table_0[curr] = max(dynamic_knapsack(items[:n-1], W),
                dynamic_knapsack(items[:n-1], W - items[n-1].w)
                + items[n-1].v)

    else:
        table_0[curr] = dynamic_knapsack(items[:n-1], W)
    
    return table_0[curr] 
    
    
def greedy_knapsack(items: list[Item], W: int) -> int:
    items.sort(key = lambda x: x.v / x.w, reverse = True)
    weight_sum = 0
    value_sum = 0
    for item in items:
        if(item.w + weight_sum <= W): 
            weight_sum += item.w
            value_sum += item.v
    
    return value_sum

def dynamic_fractional(items: list[Item], W: int) -> float:
    items.sort(key=lambda x: x.v / x.w, reverse=True)
    
    global table
    table = {}

    def helper(n: int, W: int) -> float:
        if n == 0 or W == 0:
            return 0
        curr = (n, W)
        if curr in table:
            return table[curr]
        
        if items[n-1].w <= W:
            table[curr] = max(helper(n-1, W), helper(n-1, W - items[n-1].w) + items[n-1].v)
        else:
            table[curr] = max(helper(n-1, W), items[n-1].v * (W / items[n-1].w))
        
        return table[curr]
    
    return helper(len(items), W)
    
def greedy_fractional(items: list[Item], W: int) -> int:
    items.sort(key = lambda x: x.v / x.w, reverse = True)
    knapsack = []
    weight_sum = 0
    value_sum = 0
    for item in items:
        if(item.w + weight_sum <= W): 
            weight_sum += item.w
            knapsack.append(item)
            value_sum += item.v
            
        else:
            value_sum += item.v * (W - weight_sum)/item.w
            break
            
    return value_sum

def test(ns: list[int],funcs: list[Callable],save_path: str):
        time_mat = []
        acc_matrix = []
        actual_sols = []
        i = 0
        for func in funcs:
            times = []
            acc_ratios = []
            j = 0
            for n in ns:
                min_val = 10
                max_val = 60
                
                min_weight = int(5 * sqrt(n/5))
                max_weight = int(30 * sqrt(n/5))
                W = 40 * n / 5
                items = [Item(randint(min_val,max_val),randint(min_weight, max_weight)) for _ in range(n)]
                time_start = perf_counter()
                sol = func(items, W)
                time_end = perf_counter()
                if(i == 0): 
                    actual_sols.append(sol)
                    acc_ratios.append(1)
                else:
                    acc_ratios.append(sol/actual_sols[j])
                j+=1
                 
                times.append(time_end - time_start)
            time_mat.append(times)
            acc_matrix.append(acc_ratios)
            i += 1
        i = 0
        for times in time_mat:
            plt.plot(ns, times, 'o-', label = funcs[i].__name__)
            plt.legend()
            plt.xscale('log')
            plt.yscale('log')
            plt.ylabel("Time (s)")
            plt.xlabel("N-value")
            i += 1
        plt.savefig(save_path)
        plt.clf()
        i = 0
        for acc_ratio in acc_matrix:
            plt.plot(ns, acc_ratio, 'o-', label = funcs[i].__name__)
            plt.legend()
            plt.xscale('linear')
            plt.yscale('linear')
            plt.ylabel("Accuracy ratio")
            plt.xlabel("N-value")
            i += 1
        plt.savefig("acc_"+save_path)
        
        
        
                
            
                    
            
            
        
    

if __name__ == "__main__":
    ns = [_ + 5 for _ in range(0, 100)]
    test(ns,[greedy_fractional, dynamic_fractional], "fractional_knapsack.png")
    


    
    

