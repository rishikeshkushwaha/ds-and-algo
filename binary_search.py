
nums = [-1,0,3,5,9,12]

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = int(lo + (hi-lo)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return -1


s = Solution()
print(s.search(nums=nums, target=9))
