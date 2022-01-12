class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums=sorted(nums)
        return nums
s = Solution()
nums = [0,0,1]

print(s.moveZeroes(nums=nums))
