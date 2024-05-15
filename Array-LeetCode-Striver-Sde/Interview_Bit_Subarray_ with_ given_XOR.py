# Brute Force

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         count=0
#         for i in range(len(A)):
#             xor=0
#             for j in range(i,len(A)):
#                 xor=xor^A[j]
#                 count=count+1 if xor==B else count
#         return count

#Optimal Prefix Xor
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self,A,B):
        hashmap=dict()
        hashmap[0]=1
        xor,count=0,0
        for num in A:
            xor=xor^num
            rem_xor=B^xor
            if(hashmap.get(rem_xor)!=None):
                count+=hashmap.get(rem_xor)
            hashmap[xor]=hashmap[xor]+1 if hashmap.get(xor) else 1
        return count
                
def main():
    s1=Solution()
    print(0^4)
    A=[4, 2, 2, 6, 4,6,4,3,1,8,1]
    B=6
    print(s1.solve(A,B))
main()