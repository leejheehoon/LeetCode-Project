""" https://leetcode.com/problems/valid-palindrome/ """

'''Given a string, determine if it is a palindrome
(The text is read exactly the same way even when read with reversed order)

-only considering only alphaneumeric character => A-Z, a-z, 0,9
-ignoreing cases(uppercase/lowercase)'''

# using extra memory: newStr
# using isalnum built in function

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
    
