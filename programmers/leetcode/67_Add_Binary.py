class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp_a = int(a, 2)
        temp_b = int(b, 2)

        temp = temp_a + temp_b

        num = 1
        total = 0

        while True:
            total += (temp % 2)*num
            num *= 10
            temp = temp // 2

            if temp == 0:
                break

        return str(total)


