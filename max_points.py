class Solution:

    def mostPoints(self, questions) -> int:
        n = len(questions)

        def dp(i):
            if i >= n:
                return 0
            return max(dp(i + 1), dp(i + questions[i][1] + 1) + questions[i][0])

        return dp(0)


sol = Solution()
questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
print(sol.mostPoints(questions))