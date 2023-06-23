from contextlib import contextmanager
from typing import Optional
import treact
from treact.core import Node, NodeContext


def render_html(node: Optional[Node]) -> str:
    NL = "\n"
    if not node:
        return ""
    if node.children:
        return f"""<{node.data}>
        {NL.join([render_html(child) for child in node.children])}
        </{node.data}>"""
    else:
        return f"<{node.data}/>"


@contextmanager
def HtmlRenderer(buf=None, debug=False):
    treact.__node_context__ = NodeContext(debug=debug)
    yield
    print(render_html(treact.__node_context__.root), file=buf)
