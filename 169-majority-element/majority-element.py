class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        finalresult = 0
        count = 0
        for num in nums:
            if count==0:
                finalresult = num
            if num==finalresult:
                count+=1
            else:
                count-=1
        return finalresult
