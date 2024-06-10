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
    
