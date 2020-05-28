'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    node1 = ListNode()
    node1.next = l1
    node2 = ListNode()
    node2.next = l2

    head = ListNode()
    
    merged = head
    

    while node1.next != None and node2.next != None:
        
        if node1.next.val > node2.next.val:
            node2 = node2.next
            merged.next = ListNode(node2.val)
            merged = merged.next
            
        else:
            node1 = node1.next
            merged.next = ListNode(node1.val)
            merged = merged.next

            
    if node1.next == None:
        merged.next = node2.next

    if node2.next == None:
        merged.next = node1.next

    return head.next


print(mergeTwoLists([1,2,4], [1,3,4]))