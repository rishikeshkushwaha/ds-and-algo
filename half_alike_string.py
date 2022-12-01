#1704. Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        f_h = s[:int(len(s)/2)]
        s_h = s[int(len(s)/2):]
        print(f_h, s_h)
        vowel_list = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        cf = sum([1 for x in f_h if x in vowel_list])
        cs = sum([1 for x in s_h if x in vowel_list])
        if cf==cs:
            return True
        return False

s =Solution()
print(s.halvesAreAlike('book'))

