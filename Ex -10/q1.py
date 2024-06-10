
def gale_shapely(A: list[list[int]], B : list[list[int]]) -> dict[int,int]:
    n = len(A)
    if(len(A) != len(B)): return {}
    pairs = {i : -1 for i in range(n)}

    def find_match(i: int):
        for pref in A[i]:
            if(pairs[pref] == -1): 
                pairs[pref] = i
                break
            else:
                rank_i = B[pref].index(i)
                rank_curr = B[pref].index(pairs[pref])
                if(rank_i < rank_curr):
                    old = pairs[pref]
                    pairs[pref] = i
                    find_match(old)
                    break

    for i in range(n):
        find_match(i)
    print(pairs)
    return pairs


if(__name__ == "__main__"):
    A = [
        [0,3,2,1],
        [0,1,3,2],
        [3,1,2,0],
        [2,3,1,0]
    ]
    
    B = [
        [1,2,3,0],
        [1,0,2,3],
        [2,3,1,0],
        [2,1,3,0]
    ]
    print(A)
    print(B)
    print("Matching output: ")

    gale_shapely(A, B)
    
            