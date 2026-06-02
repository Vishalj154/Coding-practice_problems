# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp.next is not None:
            if temp==temp.next
                tail.next=temp
                temp=(temp.next).next
            else:
                tail.next=temp
                temp=temp.next
        return dummy.next