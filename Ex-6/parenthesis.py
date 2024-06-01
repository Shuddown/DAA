def is_valid(expr):
    
    l_count = r_count = 0
    for char in expr:
        if char == "(": l_count += 1
        elif char == ")": r_count += 1
        if(r_count > l_count): return False
    return (r_count == l_count) 
        
        

def rem_par(expr, i = 0):
        if(is_valid(expr)):
            return expr

        if(i >= len(expr)): return ""

        choice_with = rem_par(expr, i+1)
        choice_without = rem_par(expr[:i] + expr[i+1:], i)
        return max(choice_without, choice_with, key = len)
        
    
    
if __name__ == "__main__":
    expr = " (())(()((()))("
    l = rem_par(expr)
    print(len(l) - len(expr))
    
    
    