def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if stack == []:
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else:
        return False
    
    
