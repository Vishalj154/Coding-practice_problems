class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)%2 !=0:
            return False
        for ch in s:

            if ch=='(' or ch=='{' or ch=='[':
                    stack.append(ch)
            else:
                if not stack :
                    return False
                top=stack[-1]
                if ch==')' and top=='(' or ch=='}' and top=='{' or ch==']' and top=='[':
                    stack.pop()
                else:
                    return False    

            
        if stack:
            return False
        else:
            return True

        