class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        s_p = {}
        for i,j in zip(pattern,s):
            if i not in s_p.keys():
                s_p[i] = j
            else:
                if s_p[i] != j:
                    return False
        p_s={}
        for i,j in zip(s,pattern):
            if i not in p_s.keys():
                p_s[i] = j
            else:
                if p_s[i] != j:
                    return False
        if len(pattern) != len(s):
            return False
        return True


s = Solution()
pattern = "aaa"
st = "aa aa aa aa"
print(s.wordPattern(pattern, st))
