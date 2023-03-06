class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = arr[-1]
        missing=[]
        for x in range(1,n+1):
            if x not in arr:
                missing.append(x)
        print(missing)
        if len(missing)>=k:
            return missing[k-1]
        else:
            return n+(k-len(missing))

arr = [2]
k = 1
s = Solution()
print(s.findKthPositive(arr,k))