class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = nums.count(val)
        
        for i in range(temp):
            nums.remove(val)

        return len(nums)
