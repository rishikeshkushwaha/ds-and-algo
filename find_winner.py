class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import Counter
        w = [i[0] for i in matches]
        l = [i[1] for i in matches]
        only_one_l =[k for k,v in dict(Counter(l)).items() if v==1]
        only_winner = set(w)-set(l)
        return sorted(list(only_winner)),sorted(list(only_one_l))

sol=Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(sol.findWinners(matches))