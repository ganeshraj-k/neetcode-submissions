import re
class Solution:
    def isPalindrome(self, s: str) -> bool:   


        s = ''.join(s.split(' '))
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()


        for i in range(0, len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
            
        return True

            