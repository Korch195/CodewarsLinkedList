class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    first_head = head
    second_head = head.next
    first_current = first_head
    second_current = second_head
    current = head.next.next

    while current is not None:
        first_current.next = current
        first_current = first_current.next
        current = current.next
        if current is not None:
            second_current.next = current
            second_current = second_current.next
            current = current.next

    first_current.next = None
    second_current.next = None
    return Context(first_head, second_head)
