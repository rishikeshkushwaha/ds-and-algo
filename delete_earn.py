import collections


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        # a, b = 0, 0
        def dp(i):
            if i < min(counter):
                return 0
            if i>=min(counter):
                memo[i] = max(dp(i-1), dp(i-2)+counter[i]*i)
            return memo[i]
        memo = {}
        return dp(max(counter)-1)

        #
        # for i in range(max(counter)+1):
        #     a, b = b, max(counter[i]*i + a, b)
        #     print(i, a, b)
        #
        # return b

sol = Solution()
nums = [2, 2, 3, 3, 3, 4]
print(sol.deleteAndEarn(nums))