'''

Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if head.next == None:
            return []
        
        node = head.next
        
        count = 2

        while node.next != None:
            node = node.next
            count += 1
        
        node = head.next
        c2 = 2
        
        while node.next != None:
            if c2 > count - n:
                node.val = node.next.val
                node.next = node.next.next
                return head

            c2 += 1
            node = node.next
            
        return head





