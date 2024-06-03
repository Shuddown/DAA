import random as rn

class Item:
    
    def __init__(self, value, weight) -> None:
        self.v = value
        self.w = weight
    
    def __repr__(self):
        return f"(v:{self.v}, w:{self.w})"

    
    def __str__(self):
        return f"(v:{self.v}, w:{self.w})"
    

def greedy_knapsack(items: list[Item], W: int) -> list[Item]:
    items.sort(key = lambda x: x.v / x.w, reverse = True)
    knapsack = []
    weight_sum = 0
    for item in items:
        if(item.w + weight_sum <= W): 
            weight_sum += item.w
            knapsack.append(item)
    
    return knapsack

table = {}
def dynamic_knapsack(items: list[Item], W: int)-> int:
    global table
    if(items == []): return 0
    if(W == 0): return 0
    n = len(items)
    curr = (n-1, W)
    if curr in table: return table[curr]
    
    if W - items[n-1].w >= 0: 
        table[curr] = max(dynamic_knapsack(items[:n-1], W),
                dynamic_knapsack(items[:n-1], W - items[n-1].w)
                + items[n-1].v)

    else:
        table[curr] = dynamic_knapsack(items[:n-1], W)
    
    return table[curr] 
    

    



if __name__ == "__main__":
    W = 4
    items = [Item(7, 3), Item(6,2)]
    stolen = greedy_knapsack(items, W)
    print(sum([item.v for item in stolen]))
    print(dynamic_knapsack(items, W))
    
    
    

