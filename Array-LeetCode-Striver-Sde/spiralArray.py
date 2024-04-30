class Solution:
    def addBoundaryElement(self,matrix,row_index,col_index,rows,cols,res):
        print(row_index,col_index,rows,cols)
        start_row=row_index
        start_col=col_index
        end_row=start_row+rows-1
        end_col=start_col+cols-1
        i,j=start_row,start_col

        for j in range(end_col+1):
            res.append(matrix[i][j])
        res.pop()    
        for i in range(end_row+1):
            res.append(matrix[i][j])
        res.pop()     
        for j in range(end_col,start_col-1,-1):
            res.append(matrix[i][j])
        res.pop()     
        for i in range(end_row,start_row-1,-1):
            res.append(matrix[i][j])
        res.pop()
    def spiralOrder(self, matrix) -> list():
        m=len(matrix)
        n=len(matrix[0])
        curr_rows=m
        curr_cols=n
        res=list()
        start_row=0
        while(curr_rows>0 and curr_cols>0):
            self.addBoundaryElement(matrix,start_row,start_row,curr_rows,curr_cols,res)
            curr_rows-=2
            curr_cols-=2
            start_row+=1
        return res
def main():
    matrix=[[1,2,3],
            [5,6,7],
            [9,10,11],
            [9,10,11]]
    s1=Solution()
    res=list()
    s1.addBoundaryElement(matrix,1,1,2,1,res)        
    print("hello",res)        
    print(s1.spiralOrder(matrix))
main()                
