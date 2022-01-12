
nums = [-1,0,3,5,9,12]


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_pt, right_pt = 0, len(nums) - 1
        ans = []

        for i in range(len(nums)):
            if nums[left_pt] ** 2 >= nums[right_pt] ** 2:
                ans.append(nums[left_pt]**2)
                left_pt += 1
            else:
                ans.append(nums[right_pt]**2)
                right_pt -= 1
        return ans[::-1]


s = Solution()
print(s.sortedSquares(nums=nums))