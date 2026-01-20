class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        rev=0
        while x>0:
            remain = x%10
            rev=rev*10+ remain
            x=x//10

        return rev==y
    
x=121
obj=Solution()
print(obj.isPalindrome(x))
