class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    elements = s.split(" -> ")
    if elements[0] == "None":
        return None
    head = Node(int(elements[0]))
    current = head
    for data in elements[1:-1]:
        data = int(data)
        current.next = Node(data)
        current = current.next
    return head