# 136. Single Number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = 0
        for n in nums:
            final ^= n
        return final

s = Solution()
nums = [2, 2, 4, 4, 5, 5, 1]
print(s.singleNumber(nums))
