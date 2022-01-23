
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans =[]
        while len(s) > 0:
            ans.append(s[:k])
            s = s[k:]

        if len(ans[-1]) < k:
            ans[-1]=ans[-1] + fill * (k - len(ans[-1]))
        return ans

sol = Solution()
s = "abcdefghij"
k = 3
fill="x"
target = 9
print(sol.divideString(s,k,fill))