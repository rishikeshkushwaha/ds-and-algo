
def productOfArray(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * productOfArray(arr[1:])
arr = [1,2,3,10]
print(productOfArray(arr))