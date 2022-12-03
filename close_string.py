from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        print(sorted(Counter(word1).values()))
        return sorted(Counter(word1).values())==sorted(Counter(word2).values()) and set(word1)==set(word2)



sol = Solution()

word1 = 'abc'
word2 = 'bca'

print(sol.closeStrings(word1=word1, word2=word2))