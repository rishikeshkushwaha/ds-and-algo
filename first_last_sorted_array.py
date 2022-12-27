# 34. Find First and Last Position of Element in Sorted Array

class Solution(object):

    def getLeft(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target and mid - 1 >= 0:
                    return mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def getRight(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid + 1] != target or mid == len(nums) - 1:
                    return mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.getLeft(nums, target)
        right = self.getRight(nums, target)
        return [left, right]


s = Solution()
nums = [5,7,7,8,8,10]

target = 8
print(s.searchRange(nums, target))
