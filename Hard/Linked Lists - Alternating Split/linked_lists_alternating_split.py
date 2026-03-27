class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("list must have at least two nodes")

    first_node = Node()
    second_node = Node()

    curr_first = first_node
    curr_second = second_node

    current = head
    is_first = True

    while current is not None:
        if is_first:
            curr_first.next = current
            curr_first = curr_first.next
        else:
            curr_second.next = current
            curr_second = curr_second.next

        current = current.next
        is_first = not is_first

    curr_first.next = None
    curr_second.next = None

    return Context(first_node.next, second_node.next)
