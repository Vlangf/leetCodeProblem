def reverseList(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev
