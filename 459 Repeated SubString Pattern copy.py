
# input will be a string
# take substrings of input
# multiply substring to equal the length of input
# check whether multiplied substring = input string
# Taking substrings will be limited to half the letter

class Solution: 
    def rsp(self, s: str) -> bool:
        rep = ''
        substring = len(s)
        
        
        for i in range(substring // 2):
            rep += s[i]
            if substring % len(rep) == 0:  # if not divided out, getting an answer is not possible
                if rep * (substring // len(rep)) == s:
                    return True
        return False

a = Solution() 
a.rsp("heyheyhey")
a.rsp("hello world!")