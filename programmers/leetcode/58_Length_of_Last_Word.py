class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        return len(lst[len(lst)-1])
