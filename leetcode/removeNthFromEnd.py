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

def removeNthFromEnd(head, n):
        
        #node = head.next
        i = 0
        count = 1

        #while node.next != None:
        while i < len(head):
            #node = node.next
            i+=1
            count += 1
        
        print(f"count:{count}")
        #node = head.next
        i = 0
        c2 = 1
        
        #while node.next != None:
        while i < len(head):
            if c2 >= count - n:
                #node.val = node.next.val
                #node.next = node.next.next
                print(f"count-n:{count-n}")
                print(f"c2:{c2}")
                del head[c2 - 1]
                return head

            c2 += 1
            #node = node.next
            i+=1

        print(c2)
            
        return head

print(removeNthFromEnd([1,2,3,4,5],2))
#print(removeNthFromEnd([1],1))

#1->2->3->5