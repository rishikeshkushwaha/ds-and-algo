class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        p = []

        if sum(candies) < k:
            return 0
        if sum(candies) > k:
            max_p_pile = sum(candies) // k
        if

        return p
s=Solution()
k=4
candies= [4,7,5]
print(s.maximumCandies(candies,k))