import heapq
class Item:
    
    def __init__(self, value, weight) -> None:
        self.v = value
        self.w = weight
    
    def __repr__(self):
        return f"(v:{self.v}, w:{self.w})"

    
    def __str__(self):
        return f"(v:{self.v}, w:{self.w})"

table = {}
def dynamic_fractional(items: list[Item], W: int)-> int:
    global table
    if(items == []): return 0
    if(W == 0): return 0
    n = len(items)
    curr = (n-1, W)
    if curr in table: return table[curr]
    
    if W - items[n-1].w >= 0: 
        table[curr] = max(dynamic_fractional(items[:n-1], W),
                dynamic_fractional(items[:n-1], W - items[n-1].w)
                + items[n-1].v)

    else:
        table[curr] = max(dynamic_fractional(items[:n-1], W),
                          items[n-1].v * (W / items[n-1].w))
    
    return table[curr] 
    
    