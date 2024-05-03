class Solution:
    def longestSubarrayWithSumK(self,a: [int], k: int) -> int:
        prefix_sum=dict()
        prefix_sum[0]=-1
        total_sum=0
        max_len=0
        for i in range(len(a)):
            total_sum+=a[i]
            rem_sum=total_sum-k
            if(prefix_sum.get(rem_sum)!=None):
                curr_len=i-prefix_sum.get(rem_sum)
                if(curr_len>max_len):
                    max_len=curr_len
            if(prefix_sum.get(total_sum)==None):
                prefix_sum[total_sum]=i        
        return max_len                    
        pass
def main():
    a=[4, 5, 6, 7, 8, 6, 2, 5, 3, 2, 5, 5]
    s1=Solution()
    print(s1.longestSubarrayWithSumK(a,15)) 
if __name__==main:
    main()
main()               