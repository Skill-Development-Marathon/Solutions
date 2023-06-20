def min_operations_to_make_array_equal(n):
    arr = [(2 * i) + 1 for i in range(n)]

    target = sum(arr) // n

    min_operations = 0
    for num in arr:
        min_operations += abs(num - target) / 2

    return int(min_operations)

print(min_operations_to_make_array_equal(3))