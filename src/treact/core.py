import logging
from dataclasses import dataclass, field
from typing import Optional

from src import treact

logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data):
        logger.debug("creating Node %s", data)
        self.data = data
        self.children = []
        self.depth = 0
        hierarchy = treact.__node_context__.hierarchy
        if hierarchy:
            hierarchy[-1].add_child(self)

    def __repr__(self):
        data = self.data
        children = self.children
        return f"Node({data=},{children=})"

    def add_child(self, child):
        child.depth = self.depth + 1
        self.children.append(child)

    def __enter__(self):
        logging.debug("entering %s", self.data)
        treact.__node_context__.hierarchy.append(self)

    def __exit__(self, exc_type, exc_value, trace):
        logging.debug("exiting %s", self.data)
        hierarchy = treact.__node_context__.hierarchy
        if hierarchy:
            hierarchy.pop()
        treact.__node_context__.root = self


@dataclass
class NodeContext:
    hierarchy: list = field(default_factory=list)
    root: Optional[Node] = None
