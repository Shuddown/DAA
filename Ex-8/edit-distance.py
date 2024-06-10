def editDistance(str1, str2):
    
    m = len(str1)
    n = len(str2)
    dists = [[0 for _ in range(n + 1)] for _ in range(m + 1)]


    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dists[i][j] = j
            elif j == 0:
                dists[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dists[i][j] = dists[i - 1][j - 1]
            else:
                dists[i][j] = 1 + min(dists[i][j - 1], dists[i - 1][j], dists[i - 1][j - 1])  

    return dists[m][n]
str1 = input("Give a string: ") 
str2 = input("Give another string: ")

print("Edit distance: ", editDistance(str1, str2))
