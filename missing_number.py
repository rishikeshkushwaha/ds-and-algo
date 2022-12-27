class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = [i for i in range(n + 1)]
        for i in l:
            if not i in nums:
                return i


nums = [3,0,1]
s = Solution()
print(s.missingNumber(nums))
