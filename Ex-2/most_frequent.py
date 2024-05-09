def most_frequent(string: str) -> list[str]:
    char_frequency = {}
    max_val = 0
    for char in string:
        char_frequency.setdefault(char, 0)
        char_frequency[char] += 1
        if max_val < char_frequency[char]: max_val = char_frequency[char]
    most_frequent_chars = [char for char in char_frequency if (char_frequency[char] == max_val)]
    return most_frequent_chars


test = input("Give a string: ")
print(most_frequent(test))