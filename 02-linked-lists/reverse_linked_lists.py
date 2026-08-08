class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
