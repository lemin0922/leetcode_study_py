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
        node = ListNode()
        while True:
            if l1.next is None and l2.next is None:
                break
            if isEmpty:
                if l1.val >= l2.val:
                    node.val = l2.val
                    l2 = l2.next
                else:
                    node.val = l1.val
                    l1 = l1.next
                isEmpty = False

            if l1.val >= l2.val:
                next_node = ListNode(l2.val)
                node.next = next_node
                node = next_node
                l2 = l2.next
            else:
                next_node = ListNode(l1.val)
                node.next = next_node
                node = next_node
                l1 = l1.next
        return node

if __name__ == "__main__":
    # Input: l1 = [1,2,4], l2 = [1,3,4]
    # Output: [1,1,2,3,4,4]

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    sol = Solution()
    output = sol.mergeTwoLists(list1, list2)
    a=1