# 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map_list = {}
        for i in nums:
            try:
                map_list[i] +=1
            except KeyError:
                map_list[i] =1
        return max(map_list, key = lambda x : map_list[x])

s = Solution()
nums = [1,1,2,3,5,3,2,1]
print(s.majorityElement(nums))