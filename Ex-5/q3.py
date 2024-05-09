import random as rn

def point_generator(n: int) -> list[tuple[int,int]]:
    min_x = -100
    max_x = 100
    min_y = -100
    max_y = 100
    
    def rand_tuple(min_x: int, max_x: int, min_y: int, max_y: int) -> tuple[int,int]:
        return (rn.randint(min_x, max_x), rn.randint(min_x, max_x))
    
    return [rand_tuple(min_x, max_x, min_y, max_y) for _ in range(n)]

def closest_pair(points: list[tuple[int,int]]) -> list[tuple[int,int], tuple[int,int]]:
    sorted_points = sorted(points, key = lambda x: (x[0], x[1]))
    while(len(sorted_points))