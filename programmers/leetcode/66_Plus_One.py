class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ''

        for d in digits:
            temp += str(d)

        num = int(temp) + 1

        n_list = list(map(int, str(num)))

        return n_list

