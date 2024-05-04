#Brute Force

# class Solution:
#     def isEqual(self,list1,list2):
#         list.sort(list1)
#         list.sort(list2)
#         for i in range(3):
#             if(list1[i]!=list2[i]):
#                 return False
#         return True        
#     def threeSum(self, nums) -> list[list[int]]:
#         temp_list=list()
#         length=len(nums)
#         for i in range(length):
#             for j in range(length):
#                 if(j==i):
#                     continue
#                 for k in range(length):
#                     if(k==j or k==i):
#                         continue
#                     if(nums[i]+nums[j]+nums[k])==0:
#                         temp_list.append([nums[i],nums[j],nums[k]])
#         res=list()
#         for ls in temp_list:
#             isAvailable=False
#             for lst in res:
#                 if(self.isEqual(lst,ls)):
#                     isAvailable=True
#             if(not isAvailable):
#                 res.append(ls)        
#         return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
def main():
    s1=Solution()
    nums=[-11,-3,-6,12,-15,-13,-7,-3,13,-2,-10,3,12,-12,6,-6,12,9,-2,-12,14,11,-4,11,-8,8,0,-12,4,-5,10,8,7,11,-3,7,5,-3,-11,3,11,-13,14,8,12,5,-12,10,-8,-7,5,-9,-11,-14,9,-12,1,-6,-8,-10,4,9,6,-3,-3,-12,11,9,1,8,-10,-3,2,-11,-10,-1,1,-15,-6,8,-7,6,6,-10,7,0,-7,-7,9,-8,-9,-9,-14,12,-5,-10,-15,-9,-15,-7,6,-10,5,-7,-14,3,8,2,3,9,-12,4,1,9,1,-15,-13,9,-14,11,9]
    print(s1.threeSum(nums))
main()                                    
        