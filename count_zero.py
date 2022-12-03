class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        c = 0
        while num1 >= 0 or num2 >= 0:
            if num1 > num2:
                num1 = num1 - num2
                c += 1
            elif num2 > num1:
                num2 = num2 - num1
                c += 1

            else:
                num2 = num2 - num1
                num1 = 0
                c += 1
        return c
sol = Solution()
num1 = 3
num2 = 1
print(sol.countOperations(num1, num2))
