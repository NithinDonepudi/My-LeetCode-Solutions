# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        l=set(l)
        l=sorted(l)
        list2=ListNode(1,None)
        ans=list2
        for i in l:
            temp=ListNode(i,None)
            list2.next=temp
            list2=list2.next
        list2=ans.next
        return list2
        
