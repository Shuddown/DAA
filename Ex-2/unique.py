def unique_elements(arr: list[int]) -> list[int]:
    unique_elems = {}
    for elem in arr:
        if elem not in unique_elems: unique_elems[elem] = True
        else: unique_elems[elem] = False
    return [elem for elem in unique_elems if (unique_elems[elem] == True)]

<<<<<<< HEAD
if __name__ == "__main__":
    text = input("Enter some space separated numbers: ")
    nums = [int(num) for num in text.split()]
    print(f"Unique nums: {unique_elements(nums)}")
=======

>>>>>>> origin/master

    