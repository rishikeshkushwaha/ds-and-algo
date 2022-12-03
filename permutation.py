class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(l,r):
            if l == r:
                return ans.append(nums[:])
            else:
                for i in range(l, r):
                    nums[l], nums[i] = nums[i], nums[l]
                    backtrack(l+1, r)
                    nums[l], nums[i] = nums[l], nums[i]

        ans = []
        l, r = 0, len(nums)
        backtrack(l, r)
        return ans

sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))
