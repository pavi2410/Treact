import pprint
from contextlib import contextmanager

from src import treact
from src.treact.core import NodeContext


@contextmanager
def ConsoleRenderer(buf=None):
    treact.__node_context__ = NodeContext()
    yield
    pprint.pprint(treact.__node_context__.root, indent=4, stream=buf)
