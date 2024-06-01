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

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is", lcs(X, Y))
print("Length of LCS is", lcs_recursive(X, Y))




X = "AGGTAB"
Y = "GXTXAYB"
