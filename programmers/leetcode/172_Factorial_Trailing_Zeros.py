import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = math.factorial(n)

        cnt = 0
        while True:
            temp = num % 10 
            num = num // 10
            if temp == 0:
                cnt += 1
            else:
                return cnt

            if num == 0:
                break
