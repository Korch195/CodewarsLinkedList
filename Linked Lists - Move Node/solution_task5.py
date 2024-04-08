class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError
    node_to_move = source
    source = source.next
    if dest is None:
        dest = node_to_move
        dest.next= None
    else:
        node_to_move.next = dest
        dest = node_to_move
    return Context(source, dest)