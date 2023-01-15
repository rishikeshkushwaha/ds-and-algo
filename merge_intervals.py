# 56. Merge Intervals
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged


s = Solution()
intervals = [[1, 3], [1, 2], [8, 10], [15, 18]]
print(s.merge(intervals))
