class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        s,d,c=1,0,0
        while target!=1:
            if target%2==0 and maxDoubles > 0:
                target=target/2
                maxDoubles-=1
                c+=1
            elif maxDoubles==0:
                return target-1
            else:
                target-=1
                c+=1

        return d+c
sol= Solution()
target = 5
maxDoubles=0
print(sol.minMoves(target,maxDoubles))