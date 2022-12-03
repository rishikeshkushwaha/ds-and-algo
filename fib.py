class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n >= 2:
            dp[0], dp[1] = 0, 1
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
sol = Solution()
# arr = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146,
#        282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403,
#        154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39,
#        370, 413, 168, 300, 36, 395, 204, 312, 323]
n = 2
upper=5
print(sol.fib(n=n))



def fib(k):
    arr = [0 for i in range(k+1)]
    if k== 0:
        return 0
    elif k== 1:
        return 1
    else:
        arr[0] = 0
        arr[1] = 1
        for x in range(2,k+1):
            arr[x] = arr[x-1]+arr[x-2]
    return arr[k]

print(fib(6))