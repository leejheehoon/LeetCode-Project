# Array size increasing by 1   (x)
# O(n^2)
# 1. add 0 to beg,end of previous row

class Solution:
    def generate(self, numRows: int): #-> List[List[int]]
        
        res = [[1]] # base

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] +temp[j +1])
            res.append(row)    
        return res

