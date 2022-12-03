class Solution:

    def findMaxSum(self, arr, n):

        dp = [0 for i in range(n+1)]
        if n ==1:
            return arr[0]
        elif n==2:
            return max(arr[0], arr[1])
        elif n == 3:
            dp[0] = arr[0]
            dp[1] = arr[1]
            dp[2] = arr[0]+arr[2]
            return max(dp[1], dp[2])
        else:
            dp[0] = arr[0]
            dp[1] = arr[1]
            dp[2] = arr[0] + arr[2]
            for i in range(3, n+1):
                dp[i] = arr[i] + max(dp[i-2], dp[i-3])
            return max(dp[n-2], dp[n-1])

sol = Solution()
# arr = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146,
#        282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403,
#        154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39,
#        370, 413, 168, 300, 36, 395, 204, 312, 323]
arr = [3588,8248, 1970]
n= 3
upper=5
print(sol.findMaxSum(arr=arr,n=n))