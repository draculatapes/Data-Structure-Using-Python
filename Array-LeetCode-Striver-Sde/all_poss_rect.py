#give a matrix print area of all possible rectange
class Solution(object):
    max_area=dict()
    def is_all_ones(self,matrix,rows,cols,start_row,start_col):
        for i in range(rows):
            for j in range(cols):
                if(matrix[start_row+i][start_col+j]!="1"):
                    return False
        return True
    def isAvailable(self,matrix,rows,cols,start_row,start_col):
        if(self.max_area.get((rows,cols))!=None):
            return self.max_area[(rows,cols)]
        if(rows<1 or cols<1):
            return 0    
        total_row=len(matrix)
        total_col=len(matrix[0])
        for i in range(total_row):
            for j in range(total_col):
                if((i+rows)>total_row or (j+cols)>total_col):
                    break#break out of loop
                if(self.is_all_ones(matrix,rows,cols,i,j)):
                    res=rows*cols
                    self.max_area[(rows,cols)]=rows*cols
                    return res
        res=max(self.isAvailable(matrix,rows,cols-1,0,0),self.isAvailable(matrix,rows-1,cols,0,0))
        self.max_area[(rows,cols)]=res
        return res           
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows=len(matrix)
        cols=len(matrix[0])
        return self.isAvailable(matrix,rows,cols,0,0)
def main():
    matrix=[["0","1"]] 
    s1=Solution()
    print(s1.maximalRectangle(matrix))
main()
        