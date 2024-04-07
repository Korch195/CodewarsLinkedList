class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def recursive_reverse(current, previous):
        if current is None:
            return previous
        next_node = current.next
        current.next = previous
        return recursive_reverse(next_node, current)
    return recursive_reverse(head, None)