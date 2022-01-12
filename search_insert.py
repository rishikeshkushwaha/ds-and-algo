
nums = [-1,0,3,5,9,12]
target = 10

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo+hi) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid+1
        return lo

s = Solution()
print(s.searchInsert(nums=nums, target=target))
