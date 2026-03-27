from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if index < 0:
        raise ValueError("Index cannot be less than 0")

    current = node
    count = 0

    while current:
        if count == index:
            return current

        current = current.next
        count += 1

    raise ValueError("Індекс виходить за межі списку")
