class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next          #moves 1 step
            fast=fast.next.next     #moves 2 steps
            if slow==fast :         #they met -> cycle!
                return True
                return False        #fast reached the end of the list -> no cycle

        