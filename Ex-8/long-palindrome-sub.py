d = {}

def longest_palindromic_subsequence(s: str)->int:
    n = len(s)
    if(n <= 1): return n
    if(n == 2): return 2 if s[0] == s[1] else 1
    if(d.get(s) != None): return d.get(s)
    l = longest_palindromic_subsequence(s[1:-1])
    if(s[0] == s[-1] and l == n - 2):
        d[s] = n
        return d[s] 

    d[s] = max(longest_palindromic_subsequence(s[1:]), longest_palindromic_subsequence(s[:-1]))
    return d[s]
        

print(longest_palindromic_subsequence("abcbdaabbcdccadbbdcaadbbd"))
print(d)