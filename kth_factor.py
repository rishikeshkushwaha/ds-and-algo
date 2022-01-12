# User function Template for python3
import math


class Solution:
    def kThSmallestFactor(self, N, K):
        # code here
        counter = 0
        sq = math.sqrt(N)
        for i in range(1, int(sq) + 1):
            if N % i == 0:
                counter += 1
            if counter == K:
                return i
        counter *= 2
        if (sq * sq == N):
            counter -= 1
        if (K > counter):
            return -1
        counter = 1 + counter - K
        for i in range(1, N):
            if i * i <= N:
                if (N % i == 0):
                    counter -= 1
                if (counter == 0):
                    return int(N / i)
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
        N, K = 99440 ,27
 #map(int, input().split())

        ob = Solution()
        print(ob.kThSmallestFactor(N, K))
# } Driver Code Ends