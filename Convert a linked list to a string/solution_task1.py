class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
def stringify(node: "Node"):
    return str(node)