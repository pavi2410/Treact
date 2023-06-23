from dataclasses import dataclass, field
from typing import Optional


class Node:
    def __init__(self, data):
        if __node_context__.debug:
            print("~~~~~~~~~", "creating Node", data)
        self.data = data
        self.children = []
        self.depth = 0
        hierarchy = __node_context__.hierarchy
        if hierarchy:
            hierarchy[-1].add_child(self)

    def __repr__(self):
        return f"Node({self.data=},{self.depth=})"

    def add_child(self, child):
        child.depth = self.depth + 1
        self.children.append(child)

    def __enter__(self):
        if __node_context__.debug:
            print("~~~~~~~~~", "entering", self.data)
        __node_context__.hierarchy.append(self)

    def __exit__(self, exc_type, exc_value, trace):
        if __node_context__.debug:
            print("~~~~~~~~~", "exiting", self.data)
        hierarchy = __node_context__.hierarchy
        if hierarchy:
            hierarchy.pop()
        __node_context__.root = self


@dataclass
class NodeContext:
    hierarchy: list = field(default_factory=list)
    root: Optional[Node] = None
    debug: bool = False
