class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        cnt = 1

        for i in range(1,len(nums)):
            if temp == nums[cnt]:
                nums.remove(nums[cnt])
                continue
            temp = nums[cnt]
            cnt += 1
        return cnt
            
