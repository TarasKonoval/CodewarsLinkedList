from preloaded import Node

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    values = list_repr.split(" -> ")
    head = Node(int(values[0]))
    probe = head

    for value in values[1:-1]:
        probe.next = Node(int(value))
        probe = probe.next
    return head
