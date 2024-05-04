#Brute Force \
# class Solution:
#     def numRescueBoats(self, people, limit: int) -> int:
#         saved_people=set()
#         count=0
#         size=len(people)
#         for i in range(size):
#             if(i in saved_people):
#                 continue
#             if(people[i]>=limit):
#                 count+=1
#                 saved_people.add(i)
#                 continue
#             max_sum=people[i]
#             j=i+1
#             max_index=j
#             while(j<size):
#                 curr_sum=people[i]+people[j]
#                 if(j not in saved_people and curr_sum<=limit and curr_sum>max_sum):
#                     max_index=j
#                     max_sum=curr_sum
#                     if(max_sum==limit):
#                         break
#                 j+=1 
#             if(max_sum==people[i]):
#                 saved_people.add(i)
#             else:
#                 saved_people.add(i)
#                 saved_people.add(max_index)
#             count+=1
                     
        
#         return count

#BETTER  Approach
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        list.sort(people)
        count=0
        i,j=0,len(people)-1
        while(i<=j):
            if(i==j):
                return count+1
            l_wt=people[i]
            r_wt=people[j]
            if(r_wt==limit or (l_wt+r_wt)>limit):
                j-=1
                count+=1
            else:
                i+=1
                j-=1
                count+=1
        return count
        
def main():
    s1=Solution()
    nums=[467,31,388,355,74,587,603,815,731,380,824,234,234,3,686,907,454,924,983,452,606,705,975,122,626,695,156,500,466,871,799,118,913,194,372,179,665,282,54,605,811,540,952,973,696,327,539,108,216,735,302,714,394,308,382,446,714,711,227,734,318,386,43,868,809,731,855,865,526,61,266,908,348,98,573,208,411,31,462,878,98,995,731,584,201,512,194,142,340,608,823,520,107,233,842,770,4,628,241,249,308,466,8,857,498,329,847,125,921,640,304,466,32,845,213,122,63,53,237,391,431,377,372,408,556,33,355,656,489,587,833,671,519,905,826,226,358,858,504,450,450,798,629,917,498,94,723,78,767,157,569,345,771,204,758,340,770,495,986,350,220,981,835,730,758,423,633,206,678,304,279,998,616,275,567,270,463,99,358,627,212,698,85,673,906,896,473,826,449,813,696,132,304,597,749,919,59,130,563,416,972,876,385,397,499,907,888,352,84,977,918,268,278,241,947,177,969,52,536,556,627,453,630,660,884,805,792,776,133,436,497,342,103,920,7,221,220,542,641,763,996,338,445,611,117,594,198,308,612,26,682,945,224,805,162,763,781]

    print(s1.numRescueBoats(nums,1000))
main()           

