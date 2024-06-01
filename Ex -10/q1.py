def find_match(i,A,B,pairs):
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
                find_match(old, A, B, pairs)
                break

        

def gale_shapely(A, B):
    n = len(A)
    if(len(A) != len(B)): return None
    pairs = {i : -1 for i in range(n)}
    for i in range(n):
        find_match(i, A, B, pairs)
    print(pairs)


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

    gale_shapely(A, B)
    
            