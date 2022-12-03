class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countOne = 0
        for i in nums:
            if i == 1:
                countOne += 1
        countZero = 0
        score = [countOne]
        for i in range(len(nums)):
            if nums[i]==0:
                countZero+=1
            else:
                countOne -=1
            score.append(countOne+countZero)
        max_ = max(score)
        return [i for i in range(len(score)) if score[i]==max_]

nums = [0,0,1,0]
sol = Solution()
ans = sol.maxScoreIndices(nums)
print(ans)