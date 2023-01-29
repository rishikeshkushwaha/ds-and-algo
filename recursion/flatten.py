def flatten(arr):
    if not arr:
        return []
    if type(arr[0]) == list:
        return flatten(arr[0]) + flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])


arr = [1, [2, [3, 4], [[5]]]]
print(flatten(arr))
