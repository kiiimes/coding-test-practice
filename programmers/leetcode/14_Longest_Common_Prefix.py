class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = 300
        temp_str = ''

        for s in strs:
            temp = len(s)
            if min_len > temp:
                min_len = temp
                temp_str = s
        
        answer = ''

        for i in range(min_len):
            cnt = 0
            for s in strs:
                if s[i] == temp_str[i]:
                    cnt += 1
            if cnt == len(strs):
                answer += s[i]
            else:
                break
        
        return answer



