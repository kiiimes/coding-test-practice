class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        cnt = 1
        flag = 1

        for i in range(1,len(nums)):
            if flag < 2 and temp == nums[cnt]:
                flag += 1
                cnt += 1
            elif flag >= 2 and temp == nums[cnt]:
                nums.remove(nums[cnt])
            elif temp != nums[cnt]:
                flag = 1
                temp = nums[cnt]
                cnt += 1

