def tribonacci(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0 for i in range(n + 1)]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 3:
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]
print(tribonacci(4))