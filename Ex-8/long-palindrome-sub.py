d = {}

def longest_palindromic_subsequence(s):
    if s in d:
        return d[s]
    
    n = len(s)
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2 if s[0] == s[1] else 1
    
    if s[0] == s[-1] and longest_palindromic_subsequence(s[1:-1]) == len(s) - 2:
        result = 2 + longest_palindromic_subsequence(s[1:-1])
    else:
        result = max(longest_palindromic_subsequence(s[1:]), longest_palindromic_subsequence(s[:-1]))
    
    d[s] = result
    return result

s = "bbbab"
print(longest_palindromic_subsequence(s))  # Output: 4
