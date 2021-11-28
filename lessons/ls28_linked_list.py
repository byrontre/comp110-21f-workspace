"""Simple Linked List Example."""

from __future__ import annotations

from typing import Optional


class Node:
    """Single-linked List Node."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Node):
        """Constructor."""
        self.data = data
        self.next = next


def count(head: Optional[Node]) -> int:
    """Counts up the length of a linked list."""
    if list is None:
        return 0
    else:
        return 1 + count(head.next)


third_node: Node = Node(3, None)
second_node: Node = Node(2, third_node)
a_node: Node = Node(1, second_node)
print(a_node.data)
print(count(a_node))
