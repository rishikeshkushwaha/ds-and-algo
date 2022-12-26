class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        array_size = len(cardPoints)
        window_sum = sum([cardPoints[i] for i in range(k)])
        max_sum = window_sum
        # print(0, k-1, window_sum)
        for i in range(1, array_size - k + 1):
            window_sum = window_sum - cardPoints[i - 1] + cardPoints[i + k - 1]
            # print(i, i+k-1, window_sum)
            max_sum = max(max_sum, window_sum)
        return max_sum


s = Solution()

cards = [1, 2, 3, 4, 5, 6, 1]

k = 3
print(s.maxScore(cards, k))
