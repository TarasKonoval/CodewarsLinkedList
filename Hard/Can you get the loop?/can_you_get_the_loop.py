def loop_size(node):
    node1 = node.next
    node2 = node.next.next

    while node1 != node2:
        node1 = node1.next
        node2 = node2.next.next

    count = 1
    node2 = node2.next

    while node1 != node2:
        node2 = node2.next
        count += 1

    return count
