list1 = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
list2 = ['B', 'D', 'C', 'A', 'B', 'A']

def get_greater(lens, pos, char1, char2):
    for i in range(len(pos[char1])):
        for j in range(len(pos[char2])):
            if pos[char1][i] > pos[char2][j]: lens[char1][i] =  lens[char2][j] + 1 if lens[char1][i] < lens[char2][j] else lens[char1][i]
            
             
                

def lcss(list1, list2):
    pos_dict = {}
    for i in range(len(list2)):
        if list2[i] in pos_dict: pos_dict[list2[i]].append(i)
        else: pos_dict[list2[i]] = [i]
        
    print(pos_dict)
    max_len1 = {key:([1]*len(pos_dict[key])) for key in pos_dict}
    max_len2 = [1 for _ in list1]
    
    for i in range(1, len(list1)):
        char1 = list1[i]
        for j in range(i):
            char2 = list2[j]
            indices = get_greater(pos_dict, char1, char2)
        
        
    
    

if __name__ == "__main__":
    lcss(list1, list2)
        
        