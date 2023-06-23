from contextlib import contextmanager
import treact
from treact.core import NodeContext


@contextmanager
def ConsoleRenderer(buf=None, debug=False):
    treact.__node_context__ = NodeContext(debug=debug)
    yield
    print(treact.__node_context__.root, file=buf)
