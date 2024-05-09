def sum_of_sums(n: int) -> int: return (n) * (n+1) * (2*n +1) // 6
n = int(input("Give a number: "))
print(sum_of_sums(n))


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Sum: {sum_of_sums(n)}")