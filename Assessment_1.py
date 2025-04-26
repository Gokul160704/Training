def maximumLoot(value):
    n = len(value)
    if n == 0:
        return 0
    if n == 1:
        return value[0]
    
    # Initialize an array
    arr = [0] * (n + 1)
    arr[1] = value[0]
    

    for i in range(2, n + 1):
        arr[i] = max(arr[i-1], value[i-1] + arr[i-2])
    return arr[n]

value = [6, 7, 1, 3, 8, 2, 5]
print(maximumLoot(value))  