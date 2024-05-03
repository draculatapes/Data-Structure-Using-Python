class Solution:
    def addBoundaryElement(self,matrix,row_index,col_index,rows,cols,res):
        if(rows==1 or cols==1):
            if(rows==1):
                for col_index in range(col_index,col_index+cols):
                    res.append(matrix[row_index][col_index])
            else:
                for row_index in range(row_index,row_index+rows):
                    res.append(matrix[row_index][col])        
            return 
        start_row=row_index
        start_col=col_index
        end_row=start_row+(rows-1)
        end_col=start_col+cols-1
        i,j=start_row,start_col
        for j in range(start_col,end_col+1):
            res.append(matrix[i][j])
        res.pop()    
        for i in range(start_row,end_row+1):
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
    matrix=[[4,5,6],
            [5,1,2],
            [5,2,3]]
    s1=Solution()
    res=list()
    s1.addBoundaryElement(matrix,1,1,1,1,res)
    print(res)      
    print(s1.spiralOrder(matrix))
main()                
