def max_dac(arr: list[int]) -> int:
    if len(arr) == 0: return None
    if len(arr) == 1: return arr[0]
    mid = len(arr)//2
    max_left = max_dac(arr[:mid])
    max_right = max_dac(arr[mid:])
    return max_left if max_left > max_right else max_right

if __name__ == "__main__":
    arr = [1,5,3,56,2,6,7,43,2,5,6]
    print(max_dac(arr))