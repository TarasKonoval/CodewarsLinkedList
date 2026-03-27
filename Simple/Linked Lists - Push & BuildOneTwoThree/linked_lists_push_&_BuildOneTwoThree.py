from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    new_node = Node(data)

    new_node.next = head

    return new_node

def build_one_two_three():
    link = None

    link = push(link, 3)
    link = push(link, 2)
    link = push(link, 1)

    return link
