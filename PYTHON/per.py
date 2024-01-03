import math
def calculate_permutation(n, r):
    if n < r:
        return "Invalid output"
    permutation = math.factorial(n) / math.factorial(n - r)
    return permutation
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
result = calculate_permutation(n, r)
print(f"{n}P{r} is: {result}")
