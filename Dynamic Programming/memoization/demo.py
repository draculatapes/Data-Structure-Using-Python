
class Solution(object):
    def is_all_ones(self,matrix,rows,cols,start_row,start_col):
        for i in range(rows):
            for j in range(cols):
                if(matrix[start_row+i][start_col+j]!="1"):
                    return False
        return True
s1=Solution()   
matrix=[["1","0","1","1","1"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]       
print(s1.is_all_ones(matrix,4,3,0,2,))