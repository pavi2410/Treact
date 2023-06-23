from contextlib import contextmanager
from rich.tree import Tree
from rich import print
import treact
from treact.core import NodeContext


def render_tree(node):
    if not node:
        return
    t = Tree(node.data)
    if node.children:
        for child in node.children:
            r = render_tree(child)
            if r:
                t.add(r)
    return t


@contextmanager
def RichRenderer(buf=None, debug=False):
    treact.__node_context__ = NodeContext(debug=debug)
    yield
    print(render_tree(treact.__node_context__.root), file=buf)
