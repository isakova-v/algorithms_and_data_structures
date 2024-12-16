def reverseList(head):
    prev = None
    next = None
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next
    return prev
