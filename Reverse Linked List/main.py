from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            result = None
            while head is not None:
                if result is None:
                    result = ListNode(head.val, None)
                else:
                    aux = result
                    result = ListNode(head.val, aux)
                head = head.next

        return result

class Solution:
    def reverseList(self, head: Optional[ListNode], result = None) -> Optional[ListNode]:
        if head is None:
            return None

        if result is None:
            result = ListNode(head.val, None)
        else:
            aux = result
            result = ListNode(head.val, aux)

        if head.next is None:
            return result

        return self.reverseList(head.next, result)

def print_list(root):
    count = 0
    aux = root
    while aux is not None:
        print(f"[{count}] = {aux.val}")
        aux = aux.next
        count += 1

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

list_ = Solution()
result = list_.reverseList(head)
print_list(result)


