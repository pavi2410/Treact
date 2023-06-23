from contextlib import contextmanager
from typing import Optional
from xml.dom.minidom import Document, Element

import treact
from treact.core import Node, NodeContext


def render_html(node: Optional[Node], document=Document()) -> Optional[Element]:
    if not node:
        return

    tag_name = node.data.lower().replace(' ', '-')

    element = document.createElement(tag_name)
    for child in node.children:
        element.appendChild(render_html(child, document))
    return element


@contextmanager
def HtmlRenderer(buf=None, debug=False):
    treact.__node_context__ = NodeContext(debug=debug)
    yield
    print(render_html(treact.__node_context__.root).toprettyxml(), file=buf)
