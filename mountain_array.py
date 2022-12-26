class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 1
        while i < len(arr) and arr[i] > arr[i-1]:
            i += 1
        if i == 1 or i == len(arr):
            return False
        while i < len(arr) and arr[i] < arr[i-1]:
            i += 1
        return i == len(arr)

s = Solution()
arr = [3,5,3]
print(s.validMountainArray(arr))