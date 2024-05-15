class Solution:
    def populateManhattanDis(self,grid):
        rows,cols=len(grid),len(grid[0])
        que=deque()
        visited=[[False for j in range(cols)] for i in range(rows)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    que.append([i,j])
        level=0            
        while(len(que)!=0):
            size=len(que)
            while(size>0):
                location=que.popleft()
                i,j=location[0],location[1]
                grid[i][j]=level
                visited[i][j]=True
                if(i-1>=0 and not visited[i-1][j]):
                    que.append([i-1,j])
                if(i+1<rows and not visited[i+1][j]):
                    que.append([i+1,j])
                if(j-1>=0 and not visited[i][j-1]):
                    que.append([i,j-1])
                if(j+1<cols and not visited[i][j+1]):
                    que.append([i,j+1])
                size-=1
            level+=1
                
                
            
            
    def checkIfPathValid(self,grid,factor):
        rows,cols=len(grid),len(grid[0])
        que=deque()
        visited=[[False for j in range(cols)] for i in range(rows)]
        que.append([0,0])
        if()
        
        while(len(que)!=0):
            location=que.popleft()
            i,j=location[0],location[1]  
            if(i==rows-1 and j==cols-1):
                return True
            if(i-1>=0 and not visited[i-1][j] and grid[i-1][j]>=factor):
                    que.append([i-1,j])
            if(i+1<rows and not visited[i+1][j] and grid[i+1][j]>=factor):
                que.append([i+1,j])
            if(j-1>=0 and not visited[i][j-1] and grid[i][j-1]>=factor):
                que.append([i,j-1])
            if(j+1<cols and not visited[i][j+1] and grid[i][j+1]>=factor):
                que.append([i,j+1])
            
        return False
            
            
        
        
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        res=0
        left,right=0,400
        self.populateManhattanDis(grid)
        print(grid)
        for i in range(1,800):
            if(self.checkIfPathValid(grid,i)):
                res=i
            else:
                return res
        return res
        
#         while(left<right):
#             mid=left+(right-left)/2
#             print(mid)
#             valid=self.checkIfPathValid(grid,mid)
#             if(valid):
#                 res=mid
#                 left=mid+1
#             else:
#                 right=mid-1
    
        
        