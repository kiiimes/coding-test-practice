class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        n = len(nums) / 2


        for i in nums: 
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        
        for i in dic.keys():
            if dic[i] > n :
                return i
