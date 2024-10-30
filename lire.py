import numpy as np

# Define the function L(k)
def L(k):
    return np.sum([1 / (2 * n) for n in range(1, k + 1)])

# Define the function a(k)
def a(k):
    if k == 1:
        return 1 / 2
    else:
        # Nested summation for a(k)
        result = np.sum([a(n) for n in range(1, k)])
        return L(k) - result

# Test with k = 2 (or any other value)
while True:
    try:
        k = int(input("Enter a value for k: "))
        result_L = L(k)
        result_a = a(k)

        print(f"L({k}) = {result_L}")
        print(f"a({k}) = {result_a}")
    except ValueError:
        print("Please enter an integer value.")




