class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        initial = {}

        for i in range(len(score)):
            initial[score[i][k]]=i
        desire = sorted(initial,reverse=True)
        # ans = [[0]*len(score[0]) for x in range(len(score))]
        ans=[]
        for des, init in zip(desire, score):
            ans.append( score[initial[des]])
        return ans

s = Solution()
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2

A = sorted(score, key=lambda a:a[k], reverse=True)
B = score.sort(key=lambda a:a[k], reverse=True)
print(score)