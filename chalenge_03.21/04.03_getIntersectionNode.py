# Write a program to find the node at which the intersection of two singly linked lists begins.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

[1,9,1,2,4]
[3,2,4]
a = ListNode(1)
a.next = ListNode(9)
a.next.next = ListNode(1)
a.next.next.next = ListNode(2)
a.next.next.next.next = ListNode(4)

b = ListNode(3)
b.next = ListNode(2)
b.next.next = ListNode(4)


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    l = []
    while headA:
        if headA.next:
            l.append((headA.val, headA.next.val))
        headA = headA.next

    while headB:
        if headB.next:
            if (headB.val, headB.next.val) in l:
                return headB.next.val
            headB = headB.next





print(getIntersectionNode(a, b))
