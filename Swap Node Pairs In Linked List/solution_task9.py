class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    duplicate = Node(0)
    duplicate.next = head
    prev = duplicate
    
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    
    return duplicate.next