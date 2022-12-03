class Solution:
    def generateParenthesis(self, n: int) :#-> List[str]:
        stack, res = [], []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                # print(res)
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                print(stack)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                print(stack)
                stack.pop()

        backtrack(0, 0)
        return res

sol = Solution()
sol.generateParenthesis(n=3)