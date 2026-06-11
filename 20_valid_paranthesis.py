class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            stack.append(ch)
        if len(s)%2 !=0:
            return False
        for ch in s:

            if ch==')' and '(' not in stack and len(stack)==2:
                    return False
            elif ch=='}' and '{' not in stack and len(stack)==2:
                return False
            elif ch==']' and '[' not in stack and len(stack)==2:
                return False
            else:
                return True
        