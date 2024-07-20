# 1290. Convert Binary Number in a Linked List to Integer
# Easy
# Topics
# Companies
# Hint
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

 

# Example 1:


# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
 

# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head:ListNode)->int:
        num = 0
        current = head

        while current:
            num = (num<<1) | current.val
            current = current.next
        return num
    

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example 1
head1 = create_linked_list([1, 0, 1])
solution = Solution()
print(solution.getDecimalValue(head1)) 

# Example 2
head2 = create_linked_list([0])
solution = Solution()
print(solution.getDecimalValue(head2))  