from contextlib import contextmanager
import pprint

import treact
from treact.core import NodeContext


@contextmanager
def ConsoleRenderer(buf=None):
    treact.__node_context__ = NodeContext()
    yield
    pprint.pprint(treact.__node_context__.root, indent=4, stream=buf)
