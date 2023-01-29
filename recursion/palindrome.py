def isPalindrome(s):
    if len(s)==1:
        return True
    if len(s) == 2:
        return s[0] == s[1]
    return s[0]==s[-1] and isPalindrome(s[1:-1])


s = 'tacocat'
print(isPalindrome(s))
