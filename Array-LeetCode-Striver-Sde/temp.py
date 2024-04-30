# class Solution:
#     def subarraySum(self, nums, k) -> int:
#         count=0
#         for i in range(len(nums)):
#             sum=0
#             for j in range(i,len(nums)):
#                sum+=nums[j]
#                if(sum==k):
#                     count+=1
#         return count
class Solution:
    count=0
    def findSubArray(self,nums,memory,totalSum,start,end,count,k):
        if(start>end):
            return
        if((start,end) in memory):
            return    
        memory.add((start,end))        
        if(totalSum==k):
            self.count+=1
        self.findSubArray(nums,memory,totalSum-nums[start],start+1,end,self.count,k)
        self.findSubArray(nums,memory,totalSum-nums[end],start,end-1,self.count,k)
    def subarraySum(self, nums, k) -> int:
        total_sum=0
        for num in nums:
            total_sum+=num
        memory=set()
        self.findSubArray(nums,memory,total_sum,0,len(nums)-1,self.count,k)
        return self.count
        
def main():
    s1=Solution()
    nums=[41,467,334,500,169,724,478,358,962,464,705,145,281,827,961,491,995,942,827,436,391,604,902,153,292,382,421,716,718,895,447,726,771,538,869,912,667,299,35,894,703,811,322,333,673,664,141,711,771,538,869,912,667,299,35,894,703,811,322,333,673,664,141,711,12450,0,6225,6223,2,-1,1]

    res=s1.subarraySum(nums,12450)
    print(res)                    
main()    