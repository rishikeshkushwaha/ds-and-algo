class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        import collections
        count = collections.Counter(nums)

        return [ a for a in count if count[a-1]==count[a+1]==count[a]-1 ==0]


sol = Solution()

numbers = [75,35,59,66,69,53,37,16,60,98,11,33,3,85,59,65,59,44,34,89,72,47]

upper=6
X=1212
print(sol.findLonely(nums=numbers))#,lower=lower,upper=upper))




[69,72,75,44,98,47,16,11,3,53,89,60,85,37]