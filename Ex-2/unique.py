def unique_elements(arr: list[int]) -> list[int]:
    unique_elems = {}
    for elem in arr:
        if elem not in unique_elems: unique_elems[elem] = True
        else: unique_elems[elem] = False
    return [elem for elem in unique_elems if (unique_elems[elem] == True)]



    