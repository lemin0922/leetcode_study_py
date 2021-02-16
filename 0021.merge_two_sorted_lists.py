"""
- Result -
Runtime: 48 ms, faster than 13.19% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.5 MB, less than 33.73% of Python3 online submissions for Merge Two Sorted Lists.
"""

## My code
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None

        if l1 is None or l2 is None:
            return l1 if l2 is None else l2

        isEmpty = True
        head = ListNode()
        while True:
            if l1 is None and l2 is None:
                break
            if isEmpty:
                if l1.val >= l2.val:
                    head.val = l2.val
                    l2 = l2.next
                else:
                    head.val = l1.val
                    l1 = l1.next
                isEmpty = False

            node = head
            if l1 is not None and l2 is not None:
                if l1.val >= l2.val:
                    next_node = ListNode(l2.val)
                    while node.next != None:
                        node = node.next
                    node.next = next_node
                    l2 = l2.next
                else:
                    next_node = ListNode(l1.val)
                    while node.next != None:
                        node = node.next
                    node.next = next_node
                    l1 = l1.next
            else:
                if l1 is None:
                    next_node = ListNode(l2.val)
                    while node.next != None:
                        node = node.next
                    node.next = next_node
                    l2 = l2.next
                else:
                    if l2 is None:
                        next_node = ListNode(l1.val)
                        while node.next != None:
                            node = node.next
                        node.next = next_node
                        l1 = l1.next
        return head

## Solution: https://leetcode.com/problems/merge-two-sorted-lists/discuss/1062675/Iterative-and-Recursive-with-Easy-Explanation
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        return dummy.next

if __name__ == "__main__":
    # Input: l1 = [1,2,4], l2 = [1,3,4]
    # Output: [1,1,2,3,4,4]

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    sol = Solution2()
    output = sol.mergeTwoLists(list1, list2)
    a=1