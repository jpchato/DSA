# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head):
        result = head.val
        while head.next != None:
            result = result*2 + head.next.val
            head = head.next
        return result