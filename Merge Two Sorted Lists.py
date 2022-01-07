# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode(1,None)
        ret=list3
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                temp=ListNode(list1.val,None)
                list3.next=temp
                list1=list1.next
                list3=list3.next
            elif list1.val>list2.val:
                temp=ListNode(list2.val,None)
                list3.next=temp
                list2=list2.next
                list3=list3.next
            elif list1.val==list2.val:
                list3.next=ListNode(list2.val,None)
                list3.next.next=ListNode(list1.val,None)
                list2=list2.next
                list1=list1.next
                list3=list3.next.next
        while list1!=None:
            list3.next=ListNode(list1.val,None)
            list1=list1.next
            list3=list3.next
        while list2!=None:
            list3.next=ListNode(list2.val,None)
            list2=list2.next
            list3=list3.next
        list3=ret.next
        return list3
