heights = [2,1,5,6,2,3]

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = max(heights)
        for idx, i in enumerate(heights):
            for idy, j in enumerate(heights[idx+1:]):
                print(idx, i, idy, j)
                if i >= j:
                    temp = j*abs(idx-1+idy+1)
                else:
                    temp = i*abs(idx-1+idy+1)
                if temp > ans:
                    ans = temp
        return ans


s = Solution()
print(s.largestRectangleArea(heights=heights))