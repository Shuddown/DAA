class Item:
    
    def __init__(self, value, weight) -> None:
        self.v = value
        self.w = weight
    
    def __repr__(self):
        return f"(v:{self.v}, w:{self.w})"

    
    def __str__(self):
        return f"(v:{self.v}, w:{self.w})"

def greedy_knapsack(items: list[Item], W: int) -> int:
    items.sort(key = lambda x: x.v / x.w, reverse = True)
    weight_sum = 0
    value_sum = 0
    for item in items:
        if(item.w + weight_sum <= W): 
            weight_sum += item.w
            value_sum += item.v
    
    return value_sum
