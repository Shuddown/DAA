def sum_of_sums(n: int) -> int:
    return (1/6) * (n) * (n+1) * (2*n +1)
n = int(input("Give a number: "))
print(sum_of_sums(n))