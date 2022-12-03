class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i,n in enumerate(nums):
            if n%2 ==1:
                nums[i] = n*2
        curr_min = min(nums)
        curr_max = max(nums)
        while curr_max %2 ==0:
            curr_id = nums.index(curr_max)
            nums[curr_id] = nums[curr_id] / 2
            curr_max = max(nums)

        return int(new_dev)

sol = Solution()
nums = [10,4,3]
print(sol.minimumDeviation(nums))