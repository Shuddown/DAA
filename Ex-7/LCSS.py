def lcs_recursive(X, Y, m = -1, n = -1):
    if(m == -1 or n == -1):
        m = len(X)
        n = len(Y)
    
    if m == 0 or n == 0:
        return 0
    
    if X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    
    else:
        return max(lcs_recursive(X, Y, m, n-1), lcs_recursive(X, Y, m-1, n))

def lcs(X,Y):
    m = len(X)
    n = len(Y)
    L = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if(Y[i] == X[j]): L[i+1][j+1] = min(L[i][j+1], L[i+1][j]) + 1
            else: L[i+1][j+1] = max(L[i][j+1], L[i+1][j])
    
    print(L)
    return L[n][m]


if __name__ == "__main__":
    X = "ABAABA"
    Y = "BABBAB"
    print(lcs_recursive(X,Y))
    print(lcs(X,Y))
            

