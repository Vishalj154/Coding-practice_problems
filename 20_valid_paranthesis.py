class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)%2 !=0:
            return False
        for ch in s:

            if ch=='(' or ch=='{' or ch=='[':
                    stack.append(ch)
            elif ch==')' and stack[-1]=='(':
                stack.pop()
            elif ch=='}' and stack[-1]=='{':
                stack.pop() 
            elif ch==']' and stack[-1]=='[':
                stack.pop()

            
        if stack:
            return False
        else:
            return True

        