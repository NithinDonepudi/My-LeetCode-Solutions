# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        l=[]
        list1=ListNode(1,None)
        ans=list1
        while head:
            l.append(head.val)
            head=head.next
        while val in l:
            l.remove(val)
        for i in l:
            temp=ListNode(i,None)
            list1.next=temp
            list1=list1.next
        list1=ans.next
        return list1
