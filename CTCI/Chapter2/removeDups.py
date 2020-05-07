"""
A. Write function to remove duplicates from an unsorted linked list
B. How would you solve this if a temporary buffer is not allowed?
"""
class LinkedListNode:
    def __init__(self, data):
        self.next = None
        self.data = None

def removeDups(head):

    seen = set()
    previous = LinkedListNode(data=None)

    def traverse(node, prev):
          
        if node.next.data in seen:
            prev.next = node.next.next
            return head

        else: 
            previous = node
            return head

        traverse(node.next, previous)
        
    traverse(head, previous)