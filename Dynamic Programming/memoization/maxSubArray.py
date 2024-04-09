import math
class Solution:
    def maxSubArray(self, nums) -> int:
        table=dict()
        def iterate(index,must_contain):
            if(index>=len(nums)):
                return 0 if must_contain else -math.inf
            if(table.get((index,must_contain))!=None):
                return table.get((index,must_contain))
            if(must_contain):
                res= max(0,nums[index]+iterate(index+1,True))
            else:
                res=max(iterate(index+1,False),nums[index]+iterate(index+1,True))
            table[(index,must_contain)]=res
            return res
        return iterate(0,False)
s1=Solution()
print(s1.maxSubArray([5,4,-1,7,8]))    