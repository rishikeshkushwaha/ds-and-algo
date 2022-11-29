# 724. Find Pivot Index
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        else:
            return -1

    def pivotIndex2(self, nums):
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        else:
            return -1

sol = Solution()

numbers = [1,7,3,6,5,6]

print(sol.pivotIndex2(nums=numbers))