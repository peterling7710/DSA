'''
Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''

def isPalindrome(self, head: ListNode) -> bool:
    cache = []
    
    d = ListNode()
    d.next = head
    
    node = d
    count = 0
    
    while node.next != None:
        node = node.next
        
        cache.append(node.val)
    
    
    while count < len(cache)// 2 + 1:
        
        if len(cache) == 0:
            return True
        elif cache[count] == cache[len(cache) - count - 1]:
            count += 1
        else:
            return False
        
    return True