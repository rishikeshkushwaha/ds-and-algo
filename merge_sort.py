#912. Sort an Array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr )//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

nums = [2 ,3 ,2 ,1 ,4 ,5 ,6 ,7]
print(merge_sort(nums))
