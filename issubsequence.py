#392. Is Subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        stack = list(s)

        for i in range(len(t)):
            if stack and stack[0] == t[i]:
                stack.pop(0)

        return len(stack) == 0

sol = Solution()

s ='abc'
t = 'ahbgdc'
print(sol.isSubsequence(s,t))