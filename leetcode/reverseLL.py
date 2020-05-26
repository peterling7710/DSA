'''
Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

def reverseList(head: ListNode) -> ListNode:
    vals = []

    node = head

    while node.next != None:
        node = node.next
        vals.append(node.val)
    
    node = head

    while node.next != None:
        node.val = vals.pop()
        node = node.next

    return head
    