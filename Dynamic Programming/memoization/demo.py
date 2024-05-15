def three_sum(nums,k):
    res=set()
    for i in range(len(nums)-1):
        hashset=set()
        for j in range(i+1,len(nums)):
            rem_needed=k-(nums[i]+nums[j])
            if(rem_needed in hashset):
                entry=[nums[i],nums[j],rem_needed]
                list.sort(entry)
                res.add(tuple(entry))
            hashset.add(nums[j])    
        hashset.clear()
    return list(res)
nums=[-1,0,1,-2,2,0,1,3,1,6,-3]
print(three_sum(nums,0))
