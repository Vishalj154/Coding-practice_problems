class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        count=0
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                    stack.append(ch)
            else:
                if not stack :
                    return 0
                top=stack[-1]
                if ch==')' and top=='(' or ch=='}' and top=='{' or ch==']' and top=='[':
                    count+=1
                    stack.pop()
    
        return count*2