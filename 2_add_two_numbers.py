# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        temp = l2
        carry=0
        
        while current and temp :
           sum=current.val+temp.val+carry
           carry=sum//10
           current.val+=sum%10
           current=current.next
           temp=temp.next

        while current :
            sum=current.val+carry
            carry=sum//10
            current.val=sum%10
            current=current.next
           
        while temp :
            sum=temp.val+carry
            carry=sum//10
            current.next=ListNode(sum%10)
            temp=temp.next

        if carry != 0:
            current.next = ListNode(carry)

        return l1