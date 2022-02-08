# https://leetcode.com/problems/reverse-string-ii/


class Solution:
    def reverseStr(self, s, k):                
		# Divide s into an array of substrings length k
        s = [s[i:i+k] for i in range(0, len(s), k)]
		# Reverse every other substring, beginning with s[0]
        for i in range(0, len(s), 2):
            s[i] = s[i][::-1]
		# Join array of substrings into one string and return 
        return ''.join(s)


#---------------------------------------------------------------------------------------------------------------

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r = ''
        for i in range(0, len(s), k*2):
            r += s[i:i+k][::-1] + s[i+k:i+k+k]
        return r

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(s[i:i+k][::-1] + s[i+k:i+k*2] for i in range(0, len(s), k*2))

