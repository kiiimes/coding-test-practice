class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)

        cnt = 0
        for i in range(len(temp)//2):
            if temp[i] == temp[len(temp)-i-1]:
                pass
            else:
                return False
        return True
