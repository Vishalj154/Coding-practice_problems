# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        current = dummy
        while l1 or l2 or carry :
           sum=l1.val +l2.val+carry
           carry=sum//10
           current.next=ListNode(sum%10)
           current=current.next
           l1=l1.next
           l2=l2.next

        while l1 :
            sum=l1.val+carry
            carry=sum//10
            current.next=ListNode(sum%10)
            current=current.next
            l1=l1.next
           
           
        while l2 :
           sum=l2.val+carry
           carry=sum//10
           current.next=ListNode(sum%10)
           current=current.next
           l2=l2.next

        if carry != 0:
            current.next = ListNode(carry)

        return dummy.next