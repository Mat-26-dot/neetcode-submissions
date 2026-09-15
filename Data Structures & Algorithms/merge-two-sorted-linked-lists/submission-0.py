# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy 

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        curr.next = list1 or list2

        return dummy.next

    '''Algorithm - Create dummy node and point it to -1 before index
                 - loop through
                 - compare vals
                 - move list forward 
                 - move curr pointer forward
                 Time complexity: O(n+m)
                 Space complexity O(1)'''