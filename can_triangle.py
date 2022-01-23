class Solution:
    def canMakeTriangle(self, A, N):
        #code here
        ans = []
        for i in range(len(A)-2):
            if A[i]+A[i+1] > A[i+2] and A[i+2]+A[i+1] > A[i] and A[i+2]+A[i] >A[i+1] :
                ans.append(1)
            # elif :
            #     ans.append(0)
            # elif :
            #     ans.append(0)
            else:
                ans.append(0)
        return ans

sol = Solution()
N= 5
A = {2, 10, 2, 10, 2}

print(sol.canMakeTriangle(A,N))